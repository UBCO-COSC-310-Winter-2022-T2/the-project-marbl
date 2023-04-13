
import PyQt5.QtWidgets as qt
import PyQt5.QtGui as gui
import sys
class ChatInterface(qt.QWidget):
    title : str
    left : int = 10
    right : int = 10
    width : int = 640
    height : int = 480
    
    def __init__(self) -> None:
        super().__init__()
        self
        
    def iniUI(self):
        
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_window = ChatInterface()
    login_window.show()
    sys.exit(app.exec_())
        