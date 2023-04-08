import pytest
from listener_server.ListenerServer import ListenerServer
import io
import sys
import time

_BROKER = "test.mosquitto.org" 
_SERVER_NAME = "ListenerServer"



def test_start_connection():
    # test that connection is successful
    theserver = ListenerServer(_BROKER, _SERVER_NAME)
    assert theserver._start_connection() == True

    theserver2 = ListenerServer('haha funny', _SERVER_NAME + "2")
    assert theserver2._start_connection() == False

def test_end_connection():
    theserver = ListenerServer(_BROKER, _SERVER_NAME)
    theserver._start_connection()
    assert theserver._end_connection() == True

def test_subscribe():
    theserver = ListenerServer(_BROKER, _SERVER_NAME)
    assert theserver._subscribe('test_chat') == True
    assert theserver._subscribe('') == False

def test_publish():
    theserver = ListenerServer(_BROKER, _SERVER_NAME)
    assert theserver._publish('test_chat', 'test message') == True

def test_mqtt_server():
    theserver = ListenerServer(_BROKER, _SERVER_NAME)
    theserver2 = ListenerServer(_BROKER, _SERVER_NAME + "2")
    theserver._start_connection()
    theserver2._start_connection()
    theserver._subscribe('marbltest/#')
    theserver2._subscribe('marbltest/#')

    capturedOutput = io.StringIO()                  # Create StringIO object
    sys.stdout = capturedOutput                     #  and redirect stdout.
    
    theserver._publish('marbltest', 'test message1!')
    time.sleep(1)
    assert "Received message in topic marbltest:  test message1!" in capturedOutput.getvalue()
    theserver._publish('marbltest', 'test message2!')
    time.sleep(1)
    assert "Received message in topic marbltest:  test message2!" in capturedOutput.getvalue()
    theserver._publish('marbltest/subtest', 'test message3!')
    time.sleep(1)
    assert "Received message in topic marbltest/subtest:  test message3!" in capturedOutput.getvalue()
    theserver2._publish('marbltest/subtest/subsubtest', 'test message4!')
    time.sleep(1)
    assert "Received message in topic marbltest/subtest/subsubtest:  test message4!" in capturedOutput.getvalue()
    
    sys.stdout = sys.__stdout__                     # Reset redirect.
    print ('Captured', capturedOutput.getvalue())  

    theserver._end_connection()
    theserver2._end_connection()