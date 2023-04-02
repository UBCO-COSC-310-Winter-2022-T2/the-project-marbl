from MQTTClient import MQTTClient

instance = None
def getMQTTClient(host: str) -> MQTTClient:
    global instance
    if(instance == None):
        instance = MQTTClient(host)
    return instance