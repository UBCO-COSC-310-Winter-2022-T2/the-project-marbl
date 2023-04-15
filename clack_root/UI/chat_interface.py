
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
from front_end.Getters import getSessionManager

from front_end.Getters import get_firebase_connection






class ChatInterface(QMainWindow):
    '''
    main Window body holds text promt and message hisotory and otehr chats aviable to click
    '''
    
    
    
    _title : str  
    _UI_messages = []
    _messages = []
    _chat_rooms = []
    _UI_chats_rooms = []
    _cur_chat : Chat = None # type: ignore
    _instance = None

    def __init__(self, title="--") -> None:
        '''
        create a empty chat window
        '''  
        super().__init__()
        if(self._instance != None):
            raise ReferenceError("use instance() instead")
                        
        self._instance = self
        self._session = getSessionManager().get_existing_session()
        
        
        #default param
        self._title = title
        self.setWindowTitle(self._title)
        self.setFixedSize(900,600)
        #set base layout        
        self._pageLayout = QHBoxLayout() 
        self._pageLayout#need to figure out how to limit size 
        self._chat_view_layout = QVBoxLayout()
       
        self._pageLayout.addLayout(self._chat_view_layout)
        
        #feel free to remove these as they are for testing
        #or replace them with inital loading data from db?
    
        #get and set chat rooms user has avaible 
        #get and intialize a chat if needed.
        if self._session != None:
            self.set_chats_rooms(self._session.getCurrentUser().get_chats()) # type: ignore
            if len(self._session.getCurrentUser().get_chats()) != 0: # type: ignore
                self.change_cur_chat(self._session.getCurrentUser().get_chats()[0])    # type: ignore

        #end of stuff to remove
        
        #set vars would remove because only should not carry insstance data 
        #from backend yolo.
        self.set_messages(self._messages)
        self.set_chats_rooms(self._chat_rooms)     

        self.userinput = UserInputBox(self)         
        self._chat_room_views =  ScrollableList(self._UI_chats_rooms)
        self._list_view_messages = ScrollableList(self._UI_messages)
        self._rebiuld_stack()
        self.show()
    
    def instance(self):
        if self._instance == None:
            self._instance = self.__init__()
        return self._instance
           
        

       
        
    def add_Message(self, msg : Message):
        '''
        transforms message into UI obejct adds it to the list 
        of UI objs meesages.
        '''
        self._messages.append(msg)
        #possibly save to db 
        if self._cur_chat != None:#add the new message to history
            self._cur_chat.add_message_to_history(msg)
        self._UI_messages.append(UIMessage(msg.getAuthor(),msg.getMessage(),msg.getDateTime()))
       
        
        
    def set_messages(self, messages : list):
        '''
        add a set of meesage and transform them to UI object by first clearing existing data
        
        '''  
        self._UI_messages.clear()     
        if( len(messages) == 0 or messages == None): # type: ignore
            #do nothing
            return
           
        for msg in messages:
            if isinstance(msg, Message) == True:
                msg: Message = msg
                self._UI_messages.append(UIMessage(msg.getAuthor(),msg.getMessage(),msg.getDateTime()))  
       
    
    
    def add_chat_room(self, chat : Chat):
        '''
        adds chat to Ui chat display
        '''
        self._chat_rooms.append(chat)
        self._UI_chats_rooms.append(UIChat(chat,self))
        
        
        
         
    def set_chats_rooms(self, chats :list):
        '''
        set chat rooms to be displayed to user first clearing existing data
        '''
        self._UI_chats_rooms.clear()
        if( len(chats) == 0 or chats == None): # type: ignore
           #do nothing
           return
           
        for msg in chats:
            if isinstance(msg, Chat) == True:
                msg: Chat = msg              
                self._UI_chats_rooms.append(UIChat(msg, self))  
       
    
    
    
    def _rebiuld_stack(self):
        '''
        rebiulds window with updated info
        possible better way using a actaul stack
        '''
        #clear all widgets
        self._chat_view_layout.removeWidget(self._list_view_messages)
        self._chat_view_layout.removeWidget(self.userinput)
        self._pageLayout.removeWidget(self._chat_room_views)
        
        #add them all back in
        self._pageLayout.insertWidget(0,self._chat_room_views)
        self._chat_view_layout.addWidget(self._list_view_messages)
        self._chat_view_layout.addWidget(self.userinput)
        
        widget = QWidget()       
        widget.setLayout(self._pageLayout)
        self.setCentralWidget(widget)
        
        
    def close_window(self):
        '''
        closes window
        '''
        self.close()            

        
    def change_cur_chat(self, target_chat : Chat):
        '''
        changes the view history of the chat with a new view history
        '''
        #claer old history and ui
        self._messages.clear()
        self._UI_messages.clear()
        
        #set title
        self.setWindowTitle(target_chat.chat_name)
        
        #get new history from chat
        self._messages = target_chat.message_history        
        self.set_messages(self._messages)
        
        #remove old list view widget
        self._chat_view_layout.removeWidget(self._list_view_messages)
        self._list_view_messages = ScrollableList(self._UI_messages)
        #update little clickable chat rooms
        self._chat_view_layout.removeWidget(self._chat_room_views)
        self._chat_room_views = ScrollableList(self._UI_chats_rooms)
        
        #set ref to current chat
        self._cur_chat = target_chat
        
        #add new list view from new messages 
        self._rebiuld_stack()     

    def update_UI(self):
        '''
        updates UI by recreating objects from the lists of messages and chat rooms
        then create UI objects from them and displays them
        '''
        #get new history from chat
        self.set_chats_rooms(self._chat_rooms)
        self.set_messages(self._messages)
        #remove old list view widget
        self._chat_view_layout.removeWidget(self._list_view_messages)
        self._list_view_messages = ScrollableList(self._UI_messages)
        #update little clickable chat rooms
        self._chat_view_layout.removeWidget(self._chat_room_views)
        self._chat_room_views = ScrollableList(self._UI_chats_rooms)
        
        #add new list view from new messages 
        self._rebiuld_stack()     
        
#-------------------------------------------------------------------------------    
#------------Helper classes-----------------------------------------------------
#-------------------------------------------------------------------------------
        
class UIChat(QWidget):
    '''
      chat ui element that allwos user to change chat rooms
    '''
    def __init__(self, chat : Chat, mainWindow :ChatInterface ) -> None:
        super(UIChat,self).__init__()
        from PyQt5.QtWidgets import QPushButton
        self._main_window = mainWindow
        self._cur_chat = chat
        self._layout = QHBoxLayout()
        self.setMaximumSize(200,50)
        
        self.chat_btn = QPushButton()
        self.chat_btn.setText(self._cur_chat.chat_name)
        
        self._layout.addWidget(self.chat_btn)
        self.setLayout(self._layout)
        self.chat_btn.clicked.connect(self.on_click) 
        
    def on_click(self):
        #over write me
        self._main_window._title = self._cur_chat.chat_name
        self._main_window.change_cur_chat(self._cur_chat)
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

    
    def __init__(self, mainWindow : ChatInterface ) -> None:
        super(UserInputBox,self).__init__()
        from PyQt5.QtWidgets import QHBoxLayout, QLineEdit, QPushButton




        self._main_window = mainWindow 
        self.session =  getSessionManager().get_existing_session()
        
        layout = QHBoxLayout()
        self.input = QLineEdit()
        self.enter_btn = QPushButton('Confirm')
        layout.addWidget(self.input)
        layout.addWidget(self.enter_btn)
        self.setLayout(layout)
        
        self.enter_btn.clicked.connect(self.on_click) 
        
    def on_click(self):
        #replace dummy User with Session User
        if(self.input.text != ""):
            if(self.input.text()[0] == '/'):
            #command detected
             txt : str = self.input.text()
             mydbconn = get_firebase_connection()
             mydb = mydbconn.get_database_connection()
             if txt.__contains__("/add_friend"):
                 print("friend request sent")
                 return
             elif txt.__contains__("/create"):
                name = txt.split()
                mychatid = mydb.create_group_chat(name[1])
                mydb.add_user_to_group_chat(self.session.getCurrentUser().get_username(), mychatid['name']) # type: ignore
                print("chat created")
                return
             elif txt.__contains__("/join"):
                 name = txt.split()
                 mydb.add_user_to_group_chat(self.session.getCurrentUser().get_username(), mychatid['name']) # type: ignore
                 print("jioned chat")
                 return
             else:
                 print("command unknown")
                 return
            #if /add_friend <name of friend> (send freind request)
            #if /jion <name of chat> (jion chat)
            
        
        if self.session != None or not self.input.text().__contains__("/"):
            self.session.SendMessage(self.input.text(), self._main_window._cur_chat.chat_id) # type: ignore
            # msg : Message = Message(author=self.session.getCurrentUser(),message=self.input.text())
            # self._main_window.add_Message(msg)
            self.input.setText("")
            self._main_window.update_UI()
        #send message to other participants 
        
        
        

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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_window = ChatInterface("--")
    login_window.show()
    sys.exit(app.exec_())
# #this down here is for testing purposes should be turned into 
# #white box tests but can be removed or commented out.        
# app = QApplication(sys.argv)
# login_window = ChatInterface()
# login_window.show()
# #example stuffs 
# chat = Chat(2,"yolo")
# login_window.add_chat_room(chat=chat)
# chat.message_history.append(Message("yolo",User("sally","123","emial@hot")))
# chat.message_history.append(Message("yolo",User("sally","123","emial@hot")))
# print(len(chat.message_history))
# login_window.set_messages(chat.message_history)
# login_window.set_chats_rooms([chat])
# login_window.update_UI()
# login_window.add_Message(Message("yolo",User("sally","123","emial@hot")))
# login_window.update_UI()
# sys.exit(app.exec_())

        