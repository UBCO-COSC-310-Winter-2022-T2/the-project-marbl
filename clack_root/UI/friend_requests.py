import time
from datetime import datetime
import typing
import sys
from PyQt5.QtWidgets import QWidget,QHBoxLayout, QVBoxLayout ,QApplication, QMainWindow
from PyQt5.QtGui import QPalette, QColor
from chat_interface import ScrollableList
from front_end.Message import Message
from front_end.User import User
from front_end.Chat import Chat

class RequestBoard(QMainWindow):
    
    def __init__(self):
        super(RequestBoard,self).__init__()
        self.setWindowTitle("friend Requests")
        self.setFixedSize(500,300)
        self._layout = QVBoxLayout()
        self._scrollable = ScrollableList([])

class RequestPrompt(QWidget):
    def __init__(self, request_from : User):
        super(RequestPrompt,self).__init__()
        self._layout = QHBoxLayout()
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_window = RequestBoard()
    login_window.show()
    sys.exit(app.exec_())