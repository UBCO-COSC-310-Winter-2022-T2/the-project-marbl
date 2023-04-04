
class Message:
    _text : str 
    
    def __init__(this, text : str):
        '''
        ### markdown works in here 
        ----
        #### param
        ----
        text 
        :   the messages text. and its forced to be string type by the follwing ': str' afterthe nname
        '''
        this._text = text
    
    def toString(this):
        '''
        pass keyword is used only when you have afucntion or class that you want empty 
        this refers to the vars inside the class 
        '''
        pass
        