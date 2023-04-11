import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QListWidget, QListWidgetItem, QVBoxLayout, QPushButton, QHBoxLayout, QLineEdit
from chat import ChatScreen
from functools import partial

class FriendsWindow(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Friends")

		# Create a QListWidget to display the list of friends
		self.friends_list = QListWidget()

		# Create a QLabel to display the group chats
		self.group_chats_label = QLabel("Group Chats:")

		# Create a QListWidget to display the group chats
		self.group_chats_list = QListWidget()

		#get friends and group chats
		self.get_friends_and_chat()

		# Create a QLabel and a QLineEdit widget for friend request input
		friend_req_label = QLabel('Find a Friend:')
		self.friend_req_input = QLineEdit()
		friend_req_button = QPushButton("Send Friend Request", self)
		friend_req_button.clicked.connect(lambda: self.send_friend_request(self.friend_req_input.text()))

		# Create a vertical layout and add the widgets to it
		layout = QVBoxLayout()
		layout.addWidget(self.friends_list)
		layout.addWidget(self.group_chats_label)
		layout.addWidget(self.group_chats_list)
		layout.addWidget(friend_req_label)
		layout.addWidget(self.friend_req_input)
		layout.addWidget(friend_req_button)

		self.setLayout(layout)

	def get_friends_and_chat(self):
		friends = self.get_friends()
		num_friends = 0 #counter to fill the list
		for friend in friends:
			friend_button = QPushButton(friend["username"] + "(" + friend["status"] + ")", self)
			friend_button.clicked.connect(partial(self.open_chat_window, friend["username"]))
			#to adjust variables/fix errors, you'll most probably need to edit the above line
			self.friends_list.addItem(QListWidgetItem())
			self.friends_list.setItemWidget(self.friends_list.item(num_friends), friend_button)
			num_friends = num_friends+1

		#dealing with group chats now
		# function to return group chats, say in var named group_chats
		num_group_chats = 0 #similar to num_friends
		group_chats = []
		for group_chat in group_chats:
			group_chat_button = QPushButton(group_chat.name, self)
			group_chat_button.clicked.connect(partial(self.open_chat_window, group_chat["name"]))
			self.group_chats_list.addItem(QListWidgetItem())
			self.group_chats_list.setItemWidget(self.group_chats_list.item(num_group_chats), group_chat_button)
			num_group_chats = num_group_chats+1

	def open_friends_screen(self):
		self.show()

	def open_chat_window(self, name):
		self.hide()
		self.chat_screen = ChatScreen(self, name)
		self.chat_screen.show()

	def get_friends(self):
		#get friends from db here
		#hard coding some friends for testing purposes
		friends = [{"username": "George Bush", "status": "Offline"}, {"username": "Osama Bin Laden", "status": "Online"}]
		return friends

	def send_friend_request(self, user):
		#implement the friend request feature here
		#The user field is intentionally left vague so it can be defined on username or email, whichever is more convenient
		return

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = FriendsWindow()
	window.show()
	sys.exit(app.exec_())