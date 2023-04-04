import firebase_admin
import time

cred_obj = firebase_admin.credentials.Certificate(os.path.abspath("./cosc310-marbl-firebase-adminsdk-8ced8-4927d63ad0.json"))
default_app = firebase_admin.initialize_app(cred_obj, {
	'databaseURL':'https://cosc310-marbl-default-rtdb.firebaseio.com/'
	})

from firebase_admin import db

#dbref = db.reference("/")

dbref = db.reference("/Messages/")



import paho.mqtt.client as mqtt

import re

#################################
# callback functions, will be ran once client.loop_start() is ran
def on_log(client, userdata, level, buf):
    print("long: "+buf)

def on_connect(client,userdata, flags, rc):
    if rc == 0:
        print("connected OK")
    else:
        print("Bad connection. Returned code =",rc)

def on_disconnect(client,userdata, flags, rc = 0):
    print("Disconnected result code " + str(rc))

def on_message(client, userdata, msg):
    topic=msg.topic
    m_decode = str(msg.payload.decode('utf-8','ignore'))
    print("Received message in topic " +topic+ ": ", m_decode)
    fullmsg = re.split('(\W)', m_decode) #used regex split to keep spaces
    #save message
    dbref.push().set({ 
        "author": fullmsg[0],
        "time": time.time(), # in seconds (with fractions), probably want to pass this as a part of msg from user as opposed to setting it here in the 'server'
        "msg": ''.join(fullmsg[1:])
    })
##################################

broker = "test.mosquitto.org" #our broker server
client_name = "adam"


client = mqtt.Client(client_name) #create new instance

client.on_connect = on_connect #bind call back functions
client.on_disconnect = on_disconnect 
#client.on_log = on_log
client.on_message = on_message

print("Connecting to broker", broker)
client.connect(broker)  # connect to broker
client.loop_start() #start loop (need loop to run callback functions)

client.subscribe("chatroom 1")
client.subscribe("becks room")
#client.subscribe("marbl/chatroom 1")
client.subscribe("marbl/#") # subscribe to all marbl topics (aka receive messages from every topic starting with marbl/)

while True: 
    msg = input()
    client.publish("marbl/chatroom 1", client_name + " " + msg) #send message to anyone subscribed to marbl/chatroom 1


client.loop_stop() #stop loop
client.disconnect() #disconnect