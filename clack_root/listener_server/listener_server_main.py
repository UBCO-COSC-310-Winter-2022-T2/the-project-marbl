import ListenerServer as server
import time
_BROKER = "test.mosquitto.org" 
_SERVER_NAME = "ListenerServer"

theserver = server.ListenerServer(_BROKER, _SERVER_NAME)
theserver.start_server()

#theserver._subscribe('marbltest/#')
#theserver._publish('marbltest', 'test message1!')
#time.sleep(2)
#theserver._end_connection()
