from PyQt5.QtWidgets import QApplication
from login import LoginWindow
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_screen = LoginWindow()
    login_screen.show()
    sys.exit(app.exec_())