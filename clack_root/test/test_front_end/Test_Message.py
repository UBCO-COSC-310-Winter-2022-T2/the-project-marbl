
import time
from  front_end.Message import Message
from front_end.User import User


def testSetMessage():
    u = User('bob','123','d@hot')
    m = Message("",u, 84329.83490)
    assert m.getMessage() == ""
    m.setMessage("hello world")
    assert m.getMessage() == 'hello world'

def testConstructor():
    u = User('bob','123','d@hot')
    m = Message('hi', u, 84329.83490)
    assert m.getDate() != None
    assert m.getAuthor() != None

def testFullConstructor():
    u = User('bob','123','d@hot')
    m = Message('hi', u, time.time())
    assert m.getDate() != None
    