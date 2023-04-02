from Getters import getMQTTClient

# Initialize the MQTT client
mqtt_client = getMQTTClient("test.mosquitto.org")

# Start the connection
if mqtt_client.start_connection():
    print("MQTT client connected successfully!")
else:
    print("MQTT client failed to connect")

# Publish a message to the "chatroom" chat
chat = "test"
mqtt_client.subscribe(chat)

msg = "Hello, world!"
if mqtt_client.publish(chat, msg):
    print(f"Message '{msg}' sent to chat '{chat}'")
else:
    print(f"Failed to send message to chat '{chat}'")



msg = "Anoteher message"
if mqtt_client.publish(chat, msg):
    print(f"Message '{msg}' sent to chat '{chat}'")
else:
    print(f"Failed to send message to chat '{chat}'")