import paho.mqtt.client as mqtt
import time

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
