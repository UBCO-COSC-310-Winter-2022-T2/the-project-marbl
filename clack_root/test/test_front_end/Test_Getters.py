from front_end.Getters import getMQTTClient, getSessionManager, getCommandInterface

def test_getMQTTClient():
    # test that getMQTTClient returns the same MQTTClient instance
    client1 = getMQTTClient('test_host')
    client2 = getMQTTClient('test_host')
    assert client1 is client2

    client3 = getMQTTClient('')
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
