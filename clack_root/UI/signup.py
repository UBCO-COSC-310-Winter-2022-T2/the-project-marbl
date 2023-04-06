from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
import sys

class SignupScreen(QWidget):
    def __init__(self, login_screen_to_return):
        super().__init__()

        #create a link back to login
        self.login_screen_link = login_screen_to_return

        # Set up window title and geometry
        self.setWindowTitle('Sign Up - Clack')
        self.setGeometry(100, 100, 300, 150)

        # Create widgets
        self.heading = QLabel('Enter your information:')
        self.first_name_label = QLabel('First name:')
        self.first_name_input = QLineEdit()
        self.last_name_label = QLabel('Last name:')
        self.last_name_input = QLineEdit()
        self.username_label = QLabel('Username:')
        self.username_input = QLineEdit()
        self.email_label = QLabel('Email:')
        self.email_input = QLineEdit()
        self.password_label = QLabel('Password:')
        self.password_input = QLineEdit()
        self.login_button = QPushButton('Login instead')
        self.create_an_account_button = QPushButton('Create an Account')

        # Set up layout
        layout = QVBoxLayout()
        layout.addWidget(self.heading)
        layout.addWidget(self.first_name_label)
        layout.addWidget(self.first_name_input)
        layout.addWidget(self.last_name_label)
        layout.addWidget(self.last_name_input)
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.create_an_account_button)
        layout.addWidget(self.login_button)
        self.setLayout(layout)

        # Connect login button to a slot
        self.login_button.clicked.connect(self.return_login)
        self.create_an_account_button.clicked.connect(self.create_an_account)

    def return_login(self):
        self.hide()
        self.login_screen_link.show_login_screen()

    def create_an_account(self):
        first_name = self.first_name_input.text()
        last_name = self.last_name_input.text()
        username = self.username_input.text()
        email = self.email_input.text()
        password = self.password_input.text()
        #implement/connect firebase auth signup here

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec_())