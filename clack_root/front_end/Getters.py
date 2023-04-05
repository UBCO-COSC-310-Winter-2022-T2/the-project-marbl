from front_end.MQTTClient import MQTTClient
from front_end.SessionManager import SessionManager

MQTTClient_instance = None
SessionManager_instance = None
def getMQTTClient(host: str) -> MQTTClient:
    global MQTTClient_instance
    if(MQTTClient_instance == None):
        MQTTClient_instance = MQTTClient(host)
    return MQTTClient_instance

def getSessionManager():
    global SessionManager_instance
    if(SessionManager_instance == None):
        SessionManager_instance = SessionManager()
    return SessionManager_instance