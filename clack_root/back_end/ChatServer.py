import ChatServer
class ChatServer:
    '''
    singlton pattern
    '''
    _instance : ChatServer
    
    def __init__(this):
        raise RuntimeError('use instance() instead')
    
    def instance(this) -> ChatServer:
        if(this._instance == None):
            this._instance = this.__new__()
        return this._instance