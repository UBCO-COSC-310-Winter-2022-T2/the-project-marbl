from back_end.IObserver import IObserver


class Subject:
    '''
    the subject part of the oberver pattern
    '''
    _observers = list(IObserver)
    
    @classmethod
    def subscribe(self, IObserver):
        self._observers.append(IObserver)
    
    @classmethod
    def unsubscribe(self, IObserver):
        self._observers.append(IObserver)