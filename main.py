import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog ,QApplication,QWidget,QMainWindow






class WelcomeScreen(QMainWindow):
    def __init__(self):
        super(WelcomeScreen,self).__init__()

        loadUi("welcome.ui",self)

        self.login.clicked.connect(self.gotologin)
        def gotologin(self):
            widget.addWidget(LoginScreen)

            widget.setCurrentIndex(widget.currentIndex()+1)



class LoginScreen(QMainWindow):
    def __init__(self):
        super(LoginScreen,self).__init__()
        loadUi("login.ui",self)








#main fxn .....



app = QApplication(sys.argv)
welcome = WelcomeScreen()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)
widget.setFixedHeight(500)
widget.setFixedWidth(800)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exit") 








