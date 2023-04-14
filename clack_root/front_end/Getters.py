#for retrieving and creating singleton instances

from front_end.MQTTClient import MQTTClient
from front_end.SessionManager import SessionManager
from front_end.CommandInterface import CommandInterface
from front_end.FirebaseConnection import FirebaseConnection


MQTTClient_instance = None
SessionManager_instance = None
CommandInterface_instance = None
firebase_connection = None
database_instance = None

def getMQTTClient(host: str, client_name: str) -> MQTTClient:
    global MQTTClient_instance
    if(MQTTClient_instance == None):
        MQTTClient_instance = MQTTClient(host, client_name)
        MQTTClient_instance.start_connection()
    return MQTTClient_instance

def getSessionManager():
    global SessionManager_instance
    if(SessionManager_instance == None):
        SessionManager_instance = SessionManager()
    return SessionManager_instance

def getCommandInterface():
    global CommandInterface_instance
    if(CommandInterface_instance == None):
        CommandInterface_instance = CommandInterface()
    return CommandInterface_instance

def get_firebase_connection():
    global firebase_connection
    if(firebase_connection == None):
        firebase_connection = FirebaseConnection()
    return firebase_connection