from typing_extensions import override

import back_end.IObserver as Iob
import back_end.User

class User(Iob.IObserver):
    '''
    main class for user information
    '''
    _user_name : str
    _password : str
    _email : str
    _friend_list : list()
    _chats : list()
    _online_status : bool
    
    def __init__(this):
        pass
    
    @override
    def update(state : str=None):      
        pass
    