import pytest
from front_end.MQTTClient import MQTTClient

def test_start_connection():
    # set up the MQTT client object
    client = MQTTClient('test.mosquitto.org', "testusername")
    # test that connection is successful
    assert client.start_connection() == True


    client = MQTTClient('notvalid',"testusername")
    assert client.start_connection() == False


def test_end_connection():
    client = MQTTClient('test.mosquitto.org',"testusername")
    assert client.end_connection() == True

    #client2 = MQTTClient('notvalid',"testusername")
    #assert client.end_connection() == False

def test_subscribe():
    # set up the MQTT client object
    client = MQTTClient('test.mosquitto.org',"testusername")
    assert client.subscribe('test_chat') == True
    assert client.subscribe('') == False

def test_publish():
    # set up the MQTT client object
    client = MQTTClient('test.mosquitto.org',"testusername")
    assert client.publish('test_chat', 'test message', 0) == True
    #assert client.publish('test_chat', '', 0) == False
    assert client.publish('', 'hello', 0) == False
