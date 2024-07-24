import PyQt5
from PyQt5.QtWidgets import QPushButton, QApplication, QWidget, QMainWindow, QDialog, QLineEdit
from PyQt5 import uic
import os
import sys


class ConfigureWindow(QDialog):

    def __init__(self):
        super(ConfigureWindow,self).__init__()
        uic.loadUi(f"files{os.sep}resources{os.sep}ui{os.sep}configure.ui",self)
        self.password = self.findChild(QLineEdit,"password")
        self.save_button = self.findChild(QPushButton,"saveButton")
        self.save_button.pressed.connect(self.save_password)

        if os.path.isdir(f"files{os.sep}resources{os.sep}.config") and os.path.isfile(f"files{os.sep}resources{os.sep}.config{os.sep}.pswd"):
            with open(f"files{os.sep}resources{os.sep}.config{os.sep}.pswd","r") as content:
                pswd_content = content.read()
                self.password.setText(pswd_content)


    def save_password(self):
        if self.password.text() != '':
            if os.path.isdir(f"files{os.sep}resources{os.sep}.config"):
                os.system(f"echo {self.password.text()} > files{os.sep}resources{os.sep}.config{os.sep}.pswd")
            else:
                os.system(f"mkdir files{os.sep}resources{os.sep}.config")
                with open(f"files{os.sep}resources{os.sep}.config{os.sep}.pswd","w") as contents:
                    contents.write(self.password.text())
                self.destroy()
        else:
            
            message = "Password can not be empty"
            with open(f"files{os.sep}.notif","w") as content:
                content.write(message)
            from files.constructors import notification
            notification.ui.show()
            print("sudo password can not be empty")




application = QApplication(sys.argv)
ui = ConfigureWindow()