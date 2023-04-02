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
    print("Received message: ", m_decode)
##################################

broker = "test.mosquitto.org" #our broker server
client_name = "LEVI"


client = mqtt.Client(client_name) #create new instance

client.on_connect = on_connect #bind call back functions
client.on_disconnect = on_disconnect 
#client.on_log = on_log
client.on_message = on_message

print("Connecting to broker", broker)
client.connect(broker)  # connect to broker
client.loop_start() #start loop (need loop to run callback functions)

client.subscribe("marble/chatroom 1")

while True: 
    msg = input()
    client.publish("marble/chatroom 1", client_name + " " + msg)


client.loop_stop() #stop loop
client.disconnect() #disconnect
