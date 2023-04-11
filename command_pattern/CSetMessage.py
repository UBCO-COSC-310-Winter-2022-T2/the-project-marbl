
import Icmd
import reciever

class Cmsg(Icmd.ICmd):
    
    def __init__(self, val) -> None:
        self._val = val
    
    def invoke(self):
        print("sup "+self._val)   

class Ccmplx(Icmd.ICmd):
    
    def __init__(self, val, rec : reciever.Reciever) -> None:
        self._val = val
        self._reciver = rec
    
    def invoke(self):
        self._reciver.do_thing("baller"+self._val)