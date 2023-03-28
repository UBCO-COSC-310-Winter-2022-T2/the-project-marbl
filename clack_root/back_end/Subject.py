import back_end.IObserver as Iob
class Subject:
    _listeners = list()

    
    def subscribe( listener : Iob.IObserver):
        '''
        add a listener to othis objects base
        '''
        pass
    def unsibscribe(listener : Iob.IObserver):
        '''
        remove a listener from objects base
        '''
        pass
    def notify(state : str) -> int:
        '''
        noify listners with given state
        return number of listeners notified
        '''
        return 0