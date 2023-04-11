import Icmd
import CSetMessage as c
import reciever as r


class Invoker:
    _on_start = None
    _on_finish = None
    
    def set_on_start(self, cmd : Icmd.ICmd):
        self._on_start = cmd
        
    def set_on_finish(self, cmd : Icmd.ICmd):
        self._on_finish = cmd
    
    def do_big_thing(self):
        if isinstance(self._on_start, Icmd.ICmd):
            self._on_start.invoke()
        
        if isinstance(self._on_finish, Icmd.ICmd):
            self._on_finish.invoke()

inv = Invoker()
inv.set_on_start(c.Cmsg("bbob"))
rec = r.Reciever()

inv.set_on_finish(c.Ccmplx("solo is baller", rec))

inv.do_big_thing()