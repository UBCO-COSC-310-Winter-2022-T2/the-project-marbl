import ListenerServer as server

_BROKER = "test.mosquitto.org" 
_SERVER_NAME = "ListenerServer"

theserver = server.ListenerServer(_BROKER, _SERVER_NAME)
theserver.start_server()