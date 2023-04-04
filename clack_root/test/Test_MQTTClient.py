import pytest
from front_end.MQTTClient import MQTTClient

def test_start_connection():
    # set up the MQTT client object
    client = MQTTClient('test.mosquitto.org')
    # test that connection is successful
    assert client.start_connection() == True

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
