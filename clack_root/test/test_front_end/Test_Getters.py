from front_end.Getters import getMQTTClient, getSessionManager, getCommandInterface, get_firebase_connection

def test_getMQTTClient():
    # test that getMQTTClient returns the same MQTTClient instance
    client1 = getMQTTClient('test_host', 'testusername')
    client2 = getMQTTClient('test_host','testusername')
    assert client1 is client2

    client3 = getMQTTClient('', 'testusername')
    assert client1 is client3

def test_getSessionManager():
    # test that getSessionManager returns the same instance
    client1 = getSessionManager()
    client2 = getSessionManager()
    assert client1 is client2

def test_getCommandInterface():
    # test that getCommandInterface returns the same instance
    client1 = getCommandInterface()
    client2 = getCommandInterface()
    assert client1 is client2

def test_get_firebase_connection():
    # test that get_firebase_connection returns the same instance
    client1 = get_firebase_connection()
    client2 = get_firebase_connection()
    assert client1 is not None and client1 is client2
