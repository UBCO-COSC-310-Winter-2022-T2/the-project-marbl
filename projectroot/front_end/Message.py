class Message:
    def __init__(self, message: str, author: 'User'):
        self._message = message
        self._date = datetime.now()
        self._author = author

    def getMessage(self) -> str:
        pass

    def getDate(self) -> str:
        pass

    def getAuthor(self) -> 'User':
        pass

    def setMessage(self, message: str) -> None:
        pass
