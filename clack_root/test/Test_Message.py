
import back_end.Message as msg
import back_end.User as usr

def testToString():
    assert msg.Message.toString() != None

def testSetMessage():
    m = msg.Message()
    m.setMessage("hello world")
    assert m.getMessage() == 'hello world'

def testConstructor():
    m = msg.Message('hi', usr.User())
    assert m.getDate() != None
    assert m.getUser() != None
    