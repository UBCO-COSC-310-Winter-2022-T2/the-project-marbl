

import back_end.Subject as sub
import back_end.User as usr
test_sub = sub.Subject()
test_Iob = [usr.User(),usr.User(),usr.User()]

def testSubscribe():
    test_sub.subscribe(test_Iob[0])
    assert len(test_sub.listeners) == 1
    test_sub.subscribe(test_Iob[1])
    assert len(test_sub.listeners) == 2
    test_sub.subscribe(test_Iob[2])
    assert len(test_sub.listeners) == 3
    
def testSub_set_behavour():
    test_sub.subscribe(test_Iob[1])
    assert len(test_sub.listeners) == 3

def testNofity():
     num = test_sub.notify()
     assert num == 3

def testUnSub():
    test_sub.unsibscribe(test_Iob[0])
    assert len(test_sub.listeners) == 2

def testUnSub_NoneThier():
    try:
        test_sub.unsibscribe(test_Iob[0])
    except:    
        assert len(test_sub.listeners) == 2