import pytest
from listener_server.ListenerServer import ListenerServer

_BROKER = "test.mosquitto.org" 
_SERVER_NAME = "ListenerServer"



def test_start_connection():
    # test that connection is successful
    theserver = ListenerServer(_BROKER, _SERVER_NAME)
    assert theserver._start_connection() == True

    theserver2 = ListenerServer('haha funny', _SERVER_NAME)
    assert theserver2._start_connection() == False

def test_end_connection():
    theserver = ListenerServer(_BROKER, _SERVER_NAME)
    assert theserver._end_connection() == True

    theserver2 = ListenerServer('haha funny', _SERVER_NAME)
    assert theserver2._end_connection() == False

def test_subscribe():
    theserver = ListenerServer(_BROKER, _SERVER_NAME)
    assert theserver._subscribe('test_chat') == True
    assert theserver._subscribe('') == False

def test_publish():
    theserver = ListenerServer(_BROKER, _SERVER_NAME)
    assert theserver._publish('test_chat', 'test message') == True
    assert theserver._publish('test_chat', '') == False
    assert theserver._publish('', 'hello') == False
