import os
import random
from torchelper.utils.dist_util import get_rank
from torchelper.models.model_builder import ModelBuilder
from torchelper.events.event import Event
from torchelper.events.event_center import EventCenter
from torchelper.utils import  logger
from torchelper.events.tensorboard_receiver import  TensorBoardReceiver
from torchelper.events.wechat_receiver import WechatReceiver
from tqdm import tqdm
import torch 
import time

import torch.distributed as dist
import torch.multiprocessing as mp
from torchelper.utils.config import merge_cfg
from torchelper.utils.cls_utils import get_cls, new_cls, auto_new_cls
from torchelper.data.base_dataset import get_data_loader
import torch.backends.cudnn as cudnn
import subprocess
from torchelper.utils import logger
from torchelper.models.trainable import Trainable
from torchelper.events.event_center import EventCenter

from torchelper.events.pbar_receiver import PBar
from torchelper.events.event import Event
from torchelper.utils.global_data import set_global
import pickle


def check_close_port(port):
    result = subprocess.run(['lsof', '-i:'+str(port)], stdout=subprocess.PIPE)
    out = result.stdout.decode('utf-8')

    lines = out.split('\n')
    if len(lines)<=1:
        return
    logger.warn(out)
    lines = lines[1:]
    for line in lines:
        arr = [s for s in line.split(' ') if len(s)>0]
        if len(arr)<2:
            continue
        pid = int(arr[1])
        os.system('kill '+str(pid))
        logger.warn("kill", pid)

def check_close_gpu_ids(gpu_ids):
    if not isinstance(gpu_ids, list):
        gpu_ids = [gpu_ids]
    logger.warn('kill:', gpu_ids)
    result = subprocess.run(['nvidia-smi'], stdout=subprocess.PIPE)
    out = result.stdout.decode('utf-8')

    lines = out.split('\n')
    if len(lines)<=1:
        return

    start_flag = False
    for line in lines:
        if not start_flag:
            if line.startswith('|=') and not '+' in line:
                start_flag = True
        else:
            line = ' '.join(line.split())
            arr = line.split(' ')
            if len(arr)<8:
                continue
            gpu_id = int(arr[1])
            pid = int(arr[4])
            for gid in gpu_ids:
                if gpu_id == gid and arr[6].endswith('/python'):
                    os.system('kill '+str(pid))
                    logger.warn('kill', arr[6])
      

def get_port(def_port):
    result = subprocess.run(['lsof', '-i:'+str(def_port)], stdout=subprocess.PIPE)
    out = result.stdout.decode('utf-8')

    lines = out.split('\n')
    if len(lines)<=1:
        return def_port
    return get_port(def_port+1)


def validate(model:Trainable, epoch:int, val_dataset,   gpu_num:int):
    '''执行验证集
    :param net: ModelBuilder子类实例
    :param epoch: int, 当前epoch
    :param val_dataset: 验证集
    :return: 返回描述
    :raises ValueError: 描述抛出异常场景
    '''
    model.set_eval()
    if get_rank()==0:
        model.perform_cb('on_begin_val', epoch=epoch)
    val_data:dict = {}
    pbar = PBar(val_dataset)
    for data in pbar:
        res = model.on_val(epoch, data)
        if res is None:
            continue
        for key, val in res.items():
            val_data[key] = val + val_data.get(key, 0)

    avg_val_dict = {}
    if val_data is not None:
        val_arr = []
        for key, val in val_data.items():
            avg_val_dict[key] = val_data[key] * 1.0 / len(val_dataset)

    data = pickle.dumps(avg_val_dict)
    with open(str(get_rank()), "wb+") as f:
        f.write(data)
    torch.distributed.barrier() 
    if get_rank()==0 and val_data is not None:
        names = avg_val_dict.keys()
        val_arr = []
        rs = {}
        for key in names:
            avg_v = 0
            for i in range(gpu_num):
                with open(str(i), "rb") as f:
                    data = f.read()
                avg_dict = pickle.loads(data)
                avg_v += avg_dict[key]
            avg_v = avg_v / gpu_num
            rs[key] = avg_v
            val_arr.append(key + ":" + str(avg_v))
        line = 'epoch: ' + str(epoch) + ', '  + ', '.join(val_arr)
        model.perform_cb('on_end_val', epoch=epoch, metric_dict=rs)
        logger.debug(line)
    torch.distributed.barrier() 

def init_master(cfg):
    logger.init_log(os.path.join(cfg['ckpt_dir'], "log.log"))
    wc_id = cfg.get("wechat_key", None)
    EventCenter.register([Event.Scalar, Event.Voice, Event.Pic], TensorBoardReceiver(cfg['ckpt_dir']))
    if wc_id is not None:
        EventCenter.register(Event.Scalar, WechatReceiver(wc_id))

def train(cfg):
   
    gpu_id = get_rank()
    if gpu_id == 0:
        init_master(cfg)
    train_data_cfg = merge_cfg(cfg['dataset']['train'], cfg)
    val_data_cfg =  merge_cfg(cfg['dataset']['val'], cfg)
    train_dataset = auto_new_cls(train_data_cfg)
    val_dataset = auto_new_cls(val_data_cfg)
    gpu_count = len(cfg['ori_gpu_ids'])
 
    train_dataloader = get_data_loader(cfg['batch_per_gpu'], train_dataset, num_workers=0, dist=True)
    val_dataloader = get_data_loader(cfg['batch_per_gpu'], val_dataset, dist=True)

    model:Trainable = get_cls(cfg['model'])(cfg)
 
    # builder.set_dataset(train_dataset)
    dataset_size = len(train_dataloader)
     
    step_per_epoch_per_gpu = dataset_size 
    set_global("step_per_epoch_per_gpu", step_per_epoch_per_gpu)
    set_global('gpu_count', gpu_count)
    model.perform_cb('on_begin_train', epoch=cfg['start_epoch'])
  
    for epoch in range(cfg['start_epoch'], cfg['total_epoch']):
        # validate(model, epoch, val_dataloader,  gpu_count)
        model.set_train()
        pbar = PBar(train_dataloader)
        enum_data = enumerate(pbar)
        # if gpu_id==0:
        #     pbar = tqdm(train_dataloader)
        #     enum_data = enumerate(pbar)
        # else:
        #     pbar = None
        #     enum_data =  enumerate(train_dataloader)
        EventCenter.register(Event.Scalar, pbar)
        # on begin epoch
        model.perform_cb('on_begin_epoch', epoch=epoch)
        for i, data in enum_data:
            model.on_begin_forward(data, epoch, i)
            model.perform_cb('on_begin_step', epoch=epoch, step=i)
            model.on_forward(epoch, i, data)
            model.on_end_forward(epoch, i)
            model.on_begin_backward(epoch, i)
            # 计算loss
            model.on_backward(epoch, i)
            # 多卡同步
            torch.distributed.barrier()
            model.on_end_backward(epoch, i)
            model.perform_cb('on_end_step', epoch=epoch, step=i)
            
        model.perform_cb('on_end_epoch', epoch=epoch)
        validate(model, epoch, val_dataloader, gpu_count)
    model.perform_cb('on_end_train')


def train_worker(gpu_id, nprocs, cfg, port):
    '''独立进程运行
    '''
    os.environ['NCCL_BLOCKING_WAIT']="1"
    os.environ['NCCL_ASYNC_ERROR_HANDLING']='1'
    random.seed(0)
    torch.manual_seed(0)
    cudnn.deterministic = True
    # 提升速度，主要对input shape是固定时有效，如果是动态的，耗时反而慢
    torch.backends.cudnn.benchmark = True
    dist.init_process_group(backend='nccl',
                            init_method='tcp://127.0.0.1:'+str(port),
                            world_size=len(cfg['gpu_ids']),
                            rank=gpu_id)

    torch.cuda.set_device(gpu_id)
    # 按batch分割给各个GPU
    # cfg['batch_size'] = int(cfg['batch_size'] / nprocs)
    train(cfg)

def train_main(cfg):
    check_close_gpu_ids(cfg['ori_gpu_ids'])
    # check_close_port(cfg['port'])
    gpu_nums = len(cfg['gpu_ids'])
    # if gpu_nums>1:
    port = get_port(cfg['port'])
    logger.debug('init port:', port)
    mp.spawn(train_worker, nprocs=gpu_nums, args=(gpu_nums, cfg, port ))
 
    # else:
    #     train(cfg['gpu_ids'][0], cfg, False)
