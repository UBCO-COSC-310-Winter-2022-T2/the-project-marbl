from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
import sys

class ForgotPasswordScreen(QWidget):
    def __init__(self, login_screen_to_return):
        super().__init__()
        #create link to login screen
        self.login_screen_link = login_screen_to_return

        # Set up window title and geometry
        self.setWindowTitle('Forgot Password - Clack')
        self.setGeometry(100, 100, 300, 150)

        # Create widgets
        self.heading = QLabel('Enter your email:')
        self.email_label = QLabel('Email:')
        self.email_input = QLineEdit()
        self.send_button = QPushButton('Send Email')
        self.login_button = QPushButton('Login')

        # Set up layout
        layout = QVBoxLayout()
        layout.addWidget(self.heading)
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_input)
        layout.addWidget(self.send_button)
        layout.addWidget(self.login_button)
        self.setLayout(layout)

        # Connect login button to a slot
        self.login_button.clicked.connect(self.return_login)
        self.send_button.clicked.connect(self.send_email)

    def return_login(self):
        self.hide()
        self.login_screen_link.show_login_screen()

    def send_email(self):
        email = self.email_input.text()
        #implement/connect firebase auth send password reset email here

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec_())