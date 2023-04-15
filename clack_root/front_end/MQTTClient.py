import paho.mqtt.client as mqtt
import json
from front_end.User import User
from front_end.Message import Message
from UI.chat_interface import ChatInterface

class MQTTClient:
    def __init__(self, broker_url, client_name):
        self.broker_url = broker_url
        self.client = mqtt.Client(client_name)
        self.client.on_message = self._on_message
        self.client.on_disconnect = self.on_disconnect
        self.client.on_connect = self.on_connect
        from front_end.Getters import getSessionManager
        self.mySM = getSessionManager()
        

    def start_connection(self):
        try:
            self.client.connect(self.broker_url)
            self.client.loop_start()
            return True
        except:
            return False

    def end_connection(self):
        self.client.loop_stop()
        self.client.disconnect()
        return True

    def subscribe(self, chat):
        try:
            self.client.subscribe(chat)
            return True
        except:
            return False

    def publish(self, chat, msg, qos):
        try:
            self.client.publish(chat, msg, qos)
            return True
        except:
            return False

    def on_disconnect(self, client, userdata, flags, rc):
        pass

    def on_connect(self, client, userdata, flags, rc):
        pass

####### ON MESSAGE STUFF - updates rest of client #################################
    def _process_command_sendmsg(self, msg_json, chatroom: str):
        print(msg_json["author"] + " sent a message in " +
              chatroom + " at time " + str(msg_json["time"]))
        currSession = self.mySM.get_existing_session()
        if currSession is not None: #if there is an existing session (as you probably don't want to recieve chat if not logged in)
            currUser = currSession.getCurrentUser() # type: ignore
            currChats = currUser.get_chats()
            currChat = currChats.find_chat_by_id(chatroom)
            theMessage = Message(msg_json["message"], msg_json["author"], msg_json["time"])
            currChat.add_message_to_history(theMessage)
            #update UI somehow
            # UI.notify_of_new_message(chatroomid)
            UI : ChatInterface = ChatInterface.instance() # type: ignore
            UI.update_UI()
        
    def _on_message(self, client, userdata, msg):
        topic = msg.topic
        m_decode = str(msg.payload.decode('utf-8', 'ignore'))

        # print("Received message in topic " +topic+ ": ", m_decode) #for debugging
        msg_json = json.loads(m_decode)
        command = msg_json["command"]
        match command:
            case "SENDMSG":
                # parse chatroom from topic (take off the marbl/chats/ part)
                chatroom = topic[12:]
                # remove command from the rest of the message and pass it on
                del msg_json["command"]
                self._process_command_sendmsg(msg_json, chatroom)
            case _:
                print(command + " is not a valid command")
