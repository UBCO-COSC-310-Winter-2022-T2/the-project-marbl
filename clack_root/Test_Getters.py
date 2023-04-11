from front_end.Getters import getMQTTClient, getServerInstance
	
def test_getMQTTClient():
    # test that getMQTTClient returns the same MQTTClient instance
    client1 = getMQTTClient('test_host')
    client2 = getMQTTClient('test_host')
    assert client1 is client2

    client3 = getMQTTClient('')
    assert client1 is client3

def test_getServerInstance():
    # test that getServerInstance returns the same instance
    client1 = getServerInstance('test_host')
    client2 = getServerInstance('test_host')
    assert client1 is client2

    client3 = getServerInstance('')
    assert client1 is client3
