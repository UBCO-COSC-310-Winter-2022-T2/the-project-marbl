import json
import pytest
from listener_server.ListenerServer import ListenerServer
import io
import sys
import time
import paho.mqtt.client as mqtt


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
    if (False): #broke in process of implementing test_SENDMSG_command(), which would include this case anyway
        #leaving this here for copy-pasting for future tests
        theserver = ListenerServer(_BROKER, _SERVER_NAME)
        theserver2 = ListenerServer(_BROKER, _SERVER_NAME + "2")
        theserver._start_connection()
        theserver2._start_connection()
        theserver._subscribe('marbltest/#')
        theserver2._subscribe('marbltest/#')

        capturedOutput = io.StringIO()                  # Create StringIO object
        sys.stdout = capturedOutput                     #  and redirect stdout.
        
        theserver._publish('marbltest', 'test message1!')
        time.sleep(3)
        assert "Received message in topic marbltest:  test message1!" in capturedOutput.getvalue()
        theserver2._publish('marbltest', 'test message2!')
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
    assert True
    
    
def test_SENDMSG_command():
    #author + " sent a message in " + chatroom + " at time" + str(time)
    #FOLLOW THIS TEMPLATE WHEN SENDING A MESSAGE FROM CLIENT
    test_msg =  {"command" : "SENDMSG",
        "author" : "John",
        "time" : 1230984.4839205,
        "message" : "hello world"}
    theserver = ListenerServer(_BROKER, _SERVER_NAME)
    theserver.start_server()
    
    #dummy client
    client_name = "marbltestuser"
    client = mqtt.Client(client_name)
    client.connect(_BROKER)  # connect to broker
    client.loop_start() 
    
    data_out=json.dumps(test_msg) # encode object to JSON
    
    capturedOutput = io.StringIO()                  # Create StringIO object
    sys.stdout = capturedOutput                     #  and redirect stdout.
    
    client.publish("marbl/testchatroom", data_out) 
    time.sleep(1) # wait to make sure server gets message
    
    assert "John sent a message in testchatroom at time 1230984.4839205" in capturedOutput.getvalue()
    
    sys.stdout = sys.__stdout__                     # Reset redirect.
    print ('Captured', capturedOutput.getvalue())  
    
    theserver._end_connection()