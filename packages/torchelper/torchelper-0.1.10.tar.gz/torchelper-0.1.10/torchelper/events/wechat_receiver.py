import json
import requests
import numpy as np
from torchelper.models.model_builder import ModelBuilder
from torchelper.events.receiver import Receiver
from torchelper.events.event import Event
from torchelper.models.base_model import BaseModel
from torchelper.utils.dist_util import master_only, get_bare_model

from time import strftime, localtime
from torchelper.utils import logger
import os
import socket

class WechatReceiver(Receiver):
    def __init__(self, key, is_idc=False):
        super().__init__()
        if is_idc:
            self.url = "http://in.qyapi.weixin.qq.com/cgi-bin/webhook/send?key="+key
        else:
            self.url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key="+key
        self.key = key
        self.hostname = str(socket.gethostname())
    
    def send_msg(self, data):
        try:
            post_data = json.dumps(data)
            response = requests.post(self.url,  data=post_data)
        except requests.exceptions.HTTPError as exc:
            logger.error(f"发送失败， HTTP error:{exc.response.status_code} , 原因: {exc.response.reason}")
    
        except requests.exceptions.ConnectionError:
            logger.error("发送失败，HTTP connection error!")
        except requests.exceptions.Timeout:
            logger.error("发送失败，Timeout error!")
            raise
        except requests.exceptions.RequestException:
            logger.error("发送失败, Request Exception!")
            raise
        else:
            result = None
            try:
                result = response.json()
            except json.decoder.JSONDecodeError:
                logger.error(f"服务器响应异常，状态码：{response.status_code}，响应内容：{response.text}")
    
            finally:
                return result 
 

    def get_media_id(self, path, msgtype):
        """上传资源到企业微信的存储上,msgtype有image,voice,video,file"""
        media_url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/upload_media?key={}&type={}".format(self.key, msgtype)
        try:
            with open(path, 'rb') as f:
                files = {msgtype: f}
                r = requests.post(media_url, files=files)
                re = json.loads(r.text)
                id = re.get('media_id', None)
                if id is None:
                    logger.error(re)
                return id
        except Exception as e:
            logger.error(e)
            return None
    
    def get_media_content_id(self, name, content, msgtype):
        tmp_dir_path = os.path.join(os.path.expanduser('~'), 'tmp')
        if not os.path.exists(tmp_dir_path):
            os.makedirs(tmp_dir_path)
        if msgtype=="voice":
            import wave
            dst = os.path.join(tmp_dir_path, name)
            MIN_VOL = -32768
            MAX_VOL = 32767
            if content.dtype!=np.int16:
                content = (content * np.abs(MIN_VOL)).clip(MIN_VOL, MAX_VOL).astype(np.int16)
            f = wave.open(dst, "wb")
            # 配置声道数、量化位数和取样频率
            f.setnchannels(1)
            f.setsampwidth(2)
            f.setframerate(16000)
            f.writeframes(content.tostring())
            f.close()
            id = self.get_media_id(dst, 'file')
            os.remove(dst)
            return id
        
    def send_dict_msg(self, msg:dict, msg_type):
        if msg_type == 'text':
            data = []
            for k, v in msg.items():
                v_str = str(v)
                if isinstance(v, float):
                    v_str = "%.5f"%v
                data.append("<font color=\"warning\">" + k + "</font> : " + v_str)
            data = '\n'.join(data)
            self.send_txt(data)
        elif msg_type == 'voice':
            for k, v in msg.items():
               self.send_voice(k, v) 
        elif msg_type == "file":
            data = []
            for k, v in msg.items():
               self.send_file(v)
        else:
            logger.warn("Unrecognized type " + str(msg_type))

    def send_txt(self, msg_str):
        msg = str(msg_str)
        data = {
                "msgtype": "markdown",
                "markdown": {
                        "content": "**"+self.hostname+"** \n" \
                                   + "**time : " + strftime('%Y-%m-%d %H:%M:%S',localtime())+"**\n" \
                                   + msg
                    }
                }
        self.send_msg(data)

    def send_voice(self, name, voice_content):
        id = self.get_media_content_id(name, voice_content, 'voice')
        if id is None:
            return
        data = {
                "msgtype": "file",
                "file":{
                    "media_id": id,
                }
               }
        self.send_msg(data)

    def send_file(self, file_path, type='file'):
        id = self.get_media_id(file_path, msgtype=type)
        if id is None:
            return
        data = {
                "msgtype": type,
                "file":{
                    "media_id": id,
                }
               }
        self.send_msg(data)

    def on_event(self, event: Event):
        if event.level<1:
            return
        data = event.data
        type = event.evt_type
        
        if type==Event.Scalar:
            self.send_dict_msg(data, "text")
        elif type==Event.Voice:
            self.send_dict_msg(data, "voice")
        else:
            logger.error("can not send msg with type: ", type)

    # def on_begin_train(self, model:BaseModel, epoch:int):
    #     pass

    # def on_end_train(self, model:BaseModel):
    #     pass

    # @master_only
    # def on_begin_epoch(self, model:BaseModel, epoch:int):
    #     pass
         
    # @master_only
    # def send_train_msg(self, builder:ModelBuilder):
    #     if builder is not None:
    #         dic = builder.get_scalar_dict()
    #         if dic is not None:
    #             self.send_dict_msg(dic, "text")
    #         dic = builder.get_audio_dict()
    #         if dic is not None:
    #             self.send_dict_msg(dic, "voice")

    # @master_only
    # def on_end_epoch(self, model:BaseModel, epoch:int):
    #     builder:ModelBuilder = model.get_builder()
    #     self.send_train_msg(builder)

    # def on_begin_step(self, model:BaseModel, epoch:int, step:int):
    #     pass

    # @master_only
    # def on_end_step(self, model:BaseModel, epoch:int, step:int):
    #     pass
        # builder:ModelBuilder = model.get_builder()
        # self.send_train_msg(builder)
        # builder:ModelBuilder = model.get_builder()
        # if builder is not None:
        #     dic = builder.get_scalar_dict()
        #     self.send_dict_msg(dic, "text")