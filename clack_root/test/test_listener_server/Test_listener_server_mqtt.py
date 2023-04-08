import pytest
from listener_server.ListenerServer import ListenerServer

_BROKER = "test.mosquitto.org" 
_SERVER_NAME = "ListenerServer"

theserver = ListenerServer.ListenerServer(_BROKER, _SERVER_NAME)

def test_start_connection():
    # test that connection is successful
    assert thserver._start_connection() == True

    client = MQTTClient('notvalid')
    assert client2.start_connection() == False

def test_end_connection():
    client = MQTTClient('test.mosquitto.org')
    assert client.end_connection() == True

    client2 = MQTTClient('notvalid')
    assert client.end_connection() == False

def test_subscribe():
    # set up the MQTT client object
    client = MQTTClient('test.mosquitto.org')
    assert client.subscribe('test_chat') == True
    assert client.subscribe('') == False

def test_publish():
    # set up the MQTT client object
    client = MQTTClient('test.mosquitto.org')
    assert client.publish('test_chat', 'test message') == True
    assert client.publish('test_chat', '') == False
    assert client.publish('', 'hello') == False
