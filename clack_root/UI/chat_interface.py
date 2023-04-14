
import time
from datetime import datetime
import typing
from PyQt5 import QtCore
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QWidget,QHBoxLayout, QVBoxLayout ,QApplication, QMainWindow
from PyQt5.QtGui import QPalette, QColor
import sys

from front_end.Message import Message
from front_end.User import User
from front_end.Chat import Chat







class ChatInterface(QMainWindow):
  
    _title : str  
    _UI_messages = []
    _messages = []
    _chats = []
    _UI_chats = []
    
    def __init__(self, title="--") -> None:
        '''
        create a empty chat window
        '''       
        super().__init__()
        #default param
        self._title = title
        self.setWindowTitle(self._title)
        self.setFixedSize(900,600)
        #set base layout        
        self._pageLayout = QHBoxLayout() 
        self._pageLayout#need to figure out how to limit size 
        self._chat_view_layout = QVBoxLayout()
       
        self._pageLayout.addLayout(self._chat_view_layout)
        self._chat_views =  ScrollableList(self._chats)
      
        for n in range(0,10):
           self._messages.append(Message(author=User('bob','123','@uol'), message="hellow world")) 
               
        self.set_messages(self._messages)     

        self.userinput = UserInputBox()    
        self._listViewMessages = ScrollableList(self._UI_messages)
        self._rebiuld_stack()
      
       

       
        
    def add_Message(self, msg : Message):
        '''
        transforms message into UI obejct adds it to the list 
        of UI objs meesages.
        '''
        self._UI_messages.append(UIMessage(msg.getAuthor(),msg.getMessage(),msg.getDate()))
    
    def set_messages(self, messages : list):
        '''
        add a set of meesage and transform them to UI object
        
        '''  
        self._UI_messages.clear()     
        if( len(messages) == 0 or messages == None): # type: ignore
            raise InterruptedError("messages passed is ither null or empty")
           
        for msg in messages:
            if isinstance(msg, Message) == True:
                msg: Message = msg
                self._UI_messages.append(UIMessage(msg.getAuthor(),msg.getMessage(),msg.getDate()))  
    
    
    
    def add_chat(self, chat : Chat):
        '''
        adds chat to Ui chat display
        '''
        self._UI_chats.append(UIChat(chat))
        
        
        
         
    def set_chats(self, chats :list):
        '''
        set chats to be displayed to user
        '''
        self._UI_chats.clear()
        if( len(chats) == 0 or chats == None): # type: ignore
            raise InterruptedError("messages passed is ither null or empty")
           
        for msg in chats:
            if isinstance(msg, Chat) == True:
                msg: Chat = msg
                self._UI_chats.append(UIChat(msg))  
    
    
    
    def _rebiuld_stack(self):
        '''
        rebiulds window with updated info
        possible better way using a actaul stack
        '''
        #clear all widgets
        self._chat_view_layout.removeWidget(self._listViewMessages)
        self._chat_view_layout.removeWidget(self.userinput)
        self._pageLayout.removeWidget(self._chat_views)
        
        #add them all back in
        self._pageLayout.insertWidget(0,self._chat_views)
        self._chat_view_layout.addWidget(self._listViewMessages)
        self._chat_view_layout.addWidget(self.userinput)
        
        widget = QWidget()       
        widget.setLayout(self._pageLayout)
        self.setCentralWidget(widget)
        
        
    def close_window(self):
        '''
        closes window
        '''
        self.close()    
    def _change_chat(self, chats :list):
        self._UI_chats.clear()
        self._chats.clear()
        
        self._chats = chats
        self.set_chats(self._chats)
        
        self._pageLayout.removeWidget(self._chat_views)
        self._chat_views = ScrollableList(self._UI_chats)
        
        
    def change_chat(self, target_chat : Chat):
        '''
        changes the view history of the chat with a new view history
        '''
        #claer old history and ui
        self._messages.clear()
        self._UI_messages.clear()
        
        #get new history from chat
        self._messages = target_chat.message_history
       
        self.set_messages(self._messages)
        #remove old list view widget
        self._chat_view_layout.removeWidget(self._listViewMessages)
        self._listViewMessages = ScrollableList(self._UI_messages)
        #update little clickable chat rooms
       
        
        #add new list view from new messages 
        self._rebiuld_stack()     

        
class UIChat(QWidget):
   
    def __init__(self, chat : Chat) -> None:
        super(UIChat,self).__init__()
        from PyQt5.QtWidgets import QPushButton
        self._layout = QHBoxLayout()
        self.setMaximumSize(200,50)
        self.chat_btn = QPushButton()
        self.chat_btn.setText(chat.chat_name)
        self.chat_btn.clicked.connect(self.on_click) 
        
    def on_click(self):
        #over write me
        pass

class ScrollableList(QWidget):
    '''
    Custom scollable Widget that allows Widget nesting
    '''
    def __init__(self, items) -> None:
        super(ScrollableList,self).__init__()
        self._initWidget(items)
        
    def _initWidget(self, items):
        from PyQt5.QtWidgets import QScrollArea
        listBox = QVBoxLayout(self)
        self.setLayout(listBox)

        scroll = QScrollArea(self)
        listBox.addWidget(scroll)
        scroll.setWidgetResizable(True)
        scrollContent = QWidget(scroll)

        scrollLayout = QVBoxLayout(scrollContent)
        scrollContent.setLayout(scrollLayout)
        for item in items:
            scrollLayout.addWidget(item)
        scroll.setWidget(scrollContent)

class Color(QWidget):
    '''
    helper class to show layouts
    '''
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)    

class UserInputBox(QWidget):
    '''
    custom widget that simulates a user input text box
    '''
    
    def __init__(self) -> None:
        super(UserInputBox,self).__init__()
        from PyQt5.QtWidgets import QHBoxLayout, QLineEdit, QPushButton
        layout = QHBoxLayout()
        self.input = QLineEdit()
        enter_btn = QPushButton('Confirm')
        layout.addWidget(self.input)
        layout.addWidget(enter_btn)
        self.setLayout(layout)
        

class UIMessage(QWidget):
   '''
   UI object reperstenation of Message
   '''
    
   def __init__(self, user : User, message_txt :str = "none",date : datetime=datetime.now()): 
        super(UIMessage,self).__init__()      
        from PyQt5.QtWidgets import QLabel, QHBoxLayout
        body = QVBoxLayout()
        hud = QHBoxLayout()        
        
        message = QLabel(message_txt)
        user = QLabel(user.get_username())
        time_stamp = QLabel(date.strftime("%d/%m/%Y, %H:%M:%S")) 
       
        body.addLayout(hud)
        body.addWidget(message)
        
        hud.addWidget(user)
        hud.addWidget(time_stamp)
        self.setLayout(body)

        
app = QApplication(sys.argv)
login_window = ChatInterface()
login_window.show()

chat = Chat(2,"yolo")
login_window.add_chat(chat=chat)
chat.message_history.append(Message("yolo",User("sally","123","emial@hot")))
chat.message_history.append(Message("yolo",User("sally","123","emial@hot")))
print(len(chat.message_history))
login_window.change_chat(chat)
sys.exit(app.exec_())

        