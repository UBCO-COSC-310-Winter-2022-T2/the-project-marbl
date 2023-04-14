from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
import sys

class AddFriendWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Set up window title and geometry
        self.setWindowTitle('Add Friend')
        self.setGeometry(100, 100, 300, 150)

        # Create widgets
        self.heading = QLabel('Add a new friend')
        self.name_label = QLabel('Name:')
        self.add_button = QPushButton('Add')

        # Set up layout
        layout = QVBoxLayout()
        layout.addWidget(self.heading)
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)
        layout.addWidget(self.add_button)
        self.setLayout(layout)

        # Connect add button to a slot
        self.add_button.clicked.connect(self.add_friend)

    def add_friend(self):
        name = self.name_input.text()

        # Call the function to add the friend to the database here
        # If the friend was added successfully, display a success message
        # Otherwise, display an error message

if __name__ == '__main__':
    app = QApplication([])
    add_friend_window = AddFriendWindow()
    add_friend_window.show()
    app.exec_()