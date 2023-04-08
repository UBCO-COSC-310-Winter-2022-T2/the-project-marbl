import front_end.User as User
import time
import os
import paho.mqtt.client as mqtt
import re
import pyrebase



class ListenerServer:
  def __init__(self,broker: str, server_name: str):
    #MQTT stuff
    self.client = mqtt.Client(server_name)
    self.broker = broker
    self.client.on_message = self._on_message
    self.client.on_disconnect = self._on_disconnect
    self.client.on_connect = self._on_connect
    self.client.on_log = self._on_log
    #firebase stuff
    config = {
        "apiKey": "AIzaSyAT_ILhmjVI1gv9qdWrfsFaxJSt8cvNsSw",
        "authDomain": "cosc310-marbl.firebaseapp.com",
        "databaseURL": "https://cosc310-marbl-default-rtdb.firebaseio.com",
        "storageBucket": "cosc310-marbl.appspot.com"
    }
    firebase = pyrebase.initialize_app(config)
    self.db = firebase.database()

  ##getters
  def _get_MQTT_client_instance(self):
    return self.client
  
  ##setters
  #def setIdToken(self, idToken: str):
  #  self.idToken = idToken

  ##methods
  def start_server(self):
    self._start_connection(self)
    self._subscribe(self, "marbl/#") #subscribe to all topics
  
  def _start_connection(self):
        try:
            self.client.connect(self.broker)
            self.client.loop_start()
            return True
        except:
            return False

  def _end_connection(self):
        self.client.loop_stop()
        self.client.disconnect()
        return True

  def _subscribe(self, topic : str):
        try:
            self.client.subscribe(topic)
            return True
        except:
            return False

  def _publish(self, topic : str, msg : str):
    try:
        self.client.publish(topic, msg)
        return True
    except:
        return False
        
  def _on_log(client, userdata, level, buf): #for debugging purposes
    print("long: "+buf)

  def _on_connect(client,userdata, flags, rc):
    if rc == 0:
        print("connected OK")
    else:
        print("Bad connection. Returned code =",rc)

  def _on_disconnect(client,userdata, flags, rc = 0):
    print("Disconnected result code " + str(rc))
  
    # on_message recieves all commands from user,
    # parses their params, and calls the corresponding
    # process_command() method, who will then update
    # the database and send a message through the MQTT
    # connection to notify all users that would be interested
    # that there has been a change on the server/database
  def _on_message(client, userdata, msg):
    pass

  def _process_command_sendmsg():
    pass

  def _update_db_of_sendmsg(msg : str, time : float, author : User):
    pass
