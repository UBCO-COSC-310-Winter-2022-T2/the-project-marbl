from front_end.Session import Session
import sys
import paho.mqtt.client as mqtt
import io
import json
import time
_BROKER = "test.mosquitto.org"


def _on_message(self, client, userdata, msg):
    topic = msg.topic
    m_decode = str(msg.payload.decode('utf-8', 'ignore'))

    # print("Received message in topic " +topic+ ": ", m_decode) #for debugging
    msg_json = json.loads(m_decode)
    command = msg_json["command"]
    match command:
        case "SENDMSG":
            print(msg_json["author"] + ": " + msg_json["message"])
        case _:
            print(command + " is not a valid command")


def test_send_message():

    my_test_session = Session("test", "test", "test",
                              True, "testemail", "test_username")
    # dummy client (for listening)
    client_name = "marbltestuser"
    client = mqtt.Client(client_name)
    client.connect(_BROKER)  # connect to broker
    client.on_message = _on_message
    client.loop_start()

    client.subscribe("marbl/chats/testchatroom")

    capturedOutput = io.StringIO()                  # Create StringIO object
    sys.stdout = capturedOutput  # and redirect stdout.

    my_test_session.SendMessage("hello world!", "testchatroom")
    time.sleep(1)  # wait to make sure client gets message

    assert "test_username: hello world!" in capturedOutput.getvalue()

    sys.stdout = sys.__stdout__                     # Reset redirect.
    print('Captured', capturedOutput.getvalue())

    client.disconnect()
