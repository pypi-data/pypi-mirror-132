class Event:
    
    Scalar="evt_scalar"
    Voice="evt_voice"
    Pic="evt_pic"
    Level_step = 0
    Level_epoch = 1
    Level_val = 2
 

    def __init__(self, evt_type:str, data:dict, level:int=0, extra:dict={}):
        self.evt_type = evt_type
        self.data = data
        self.extra = extra
        self.level=level

    def wrap_extra(self, key, val):
        self.extra = {
            key:val
        }