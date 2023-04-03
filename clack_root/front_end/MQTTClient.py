import paho.mqtt.client as mqtt

class MQTTClient:
    def __init__(self, broker_url):
        self.broker_url = broker_url
        self.client = mqtt.Client()
        self.client.on_message = self.on_message
        self.client.on_disconnect = self.on_disconnect
        self.client.on_connect = self.on_connect

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

    def publish(self, chat, msg):
        try:
            self.client.publish(chat, msg)
            return True
        except:
            return False

    def on_message(self, client, userdata, msg):
        pass

    def on_disconnect(self, client, userdata, flags, rc):
        pass

    def on_connect(self, client, userdata, flags, rc):
        pass