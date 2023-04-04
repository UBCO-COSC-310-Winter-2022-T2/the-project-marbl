from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
import sys
from signup import SignupScreen
from forgot import ForgotPasswordScreen

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Set up window title and geometry
        self.setWindowTitle('Login to Clack')
        self.setGeometry(100, 100, 300, 150)

        # Create widgets
        self.heading = QLabel('Enter your email and password:')
        self.email_label = QLabel('Email:')
        self.email_input = QLineEdit()
        self.password_label = QLabel('Password:')
        self.password_input = QLineEdit()
        self.login_button = QPushButton('Login')
        self.forgot_password_button = QPushButton('Forgot Password?')
        self.create_an_account_button = QPushButton('Create an Account')

        # Set up layout
        layout = QVBoxLayout()
        layout.addWidget(self.heading)
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)
        layout.addWidget(self.forgot_password_button)
        layout.addWidget(self.create_an_account_button)
        self.setLayout(layout)

        # Connect login button to a slot
        self.login_button.clicked.connect(self.login)
        self.forgot_password_button.clicked.connect(self.switch_forgot_password_screen)
        self.create_an_account_button.clicked.connect(self.switch_create_an_account_screen)

    def switch_forgot_password_screen(self):
        self.hide()
        self.forgot_password_screen = ForgotPasswordScreen(self)
        self.forgot_password_screen.show()

    def switch_create_an_account_screen(self):
        self.hide()
        self.signup_screen = SignupScreen(self)
        self.signup_screen.show()

    def show_login_screen(self):
        self.show()

    def login(self):
        email = self.email_input.text()
        password = self.password_input.text()
        #implement/connect firebase auth login here

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec_())