from typing_extensions import override
from back_end.IObserver import IObserver


class User(IObserver):
    '''
    user data containter 
    '''
    
    @override
    def update(self) -> None:
        return super().update()