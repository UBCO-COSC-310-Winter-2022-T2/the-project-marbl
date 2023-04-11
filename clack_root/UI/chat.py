import sys
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QLineEdit, QPushButton, QHBoxLayout, QApplication, QListWidget, QListWidgetItem

class ChatScreen(QWidget):
	def __init__(self, friends_screen, name):
		super().__init__()
		self.friends_screen = friends_screen
		self.setWindowTitle(name)

		# Load previous messages shared with the friend
		self.messages_list = QListWidget()
		self.get_messages(name)

		# Create input box and send button for sending messages
		self.input_box = QLineEdit()
		self.send_button = QPushButton("Send")
		self.send_button.clicked.connect(self.send_message)

		# Create back button to return to the FriendsScreen
		self.back_button = QPushButton("Back")
		self.back_button.clicked.connect(self.return_to_friends)
		# Create a QHBoxLayout to hold the input box and send button
		input_layout = QHBoxLayout()
		input_layout.addWidget(self.input_box)
		input_layout.addWidget(self.send_button)
		# Create a QVBoxLayout to hold the messages, input layout, and back button
		layout = QVBoxLayout()
		layout.addWidget(self.back_button)
		layout.addWidget(self.messages_list)
		layout.addLayout(input_layout)
		self.setLayout(layout)

	def send_message(self):
		message = self.input_box.text()
		# Send the message to the friend
		self.input_box.clear()

	def return_to_friends(self):
		self.friends_screen.open_friends_screen()
		self.close()

	def get_messages(self, name):
		#get messages for the friend
		#hard coding some messages for testing
		#we can add timestamps if mqtt supports that
		prev_messages = [{"sender": name, "msg": "Hey! I need your help with something"}, {"sender": "You", "msg": "Yeah what's up?"}, {"sender": name, "msg": "I'm trying to handle road rage here, but I don't know what to do. Any ideas on how to run the country?"}]
		num_messages = 1 #0 is the following

		#declaration/heading for the chat
		self.message1 = QTextEdit()
		self.message1.setReadOnly(True)
		self.message1.setText("Previous messages with " + name)
		self.messages_list.addItem(QListWidgetItem())
		self.messages_list.setItemWidget(self.messages_list.item(0), self.message1)

		for message in prev_messages:
			message_box = QTextEdit()
			message_box.setReadOnly(True)
			message_box.setText(message["sender"] + ": " + message["msg"])
			self.messages_list.addItem(QListWidgetItem())
			self.messages_list.setItemWidget(self.messages_list.item(num_messages), message_box)
			num_messages = num_messages+1

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = ChatScreen()
	window.show()
	sys.exit(app.exec_())