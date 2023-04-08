import listener_server as server

_BROKER = "test.mosquitto.org" 
_SERVER_NAME = "ListenerServer"

theserver = server.listener_server(_BROKER, _SERVER_NAME)
theserver.start_server()