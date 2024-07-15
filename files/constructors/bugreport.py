import PyQt5
from PyQt5.QtWidgets import QPushButton, QTextEdit, QApplication, QWidget, QMainWindow, QDialog, QLineEdit
from PyQt5 import uic
from files.resources.icons import icons
import os
import sys
import requests


class BugReport(QDialog):

    def __init__(self):
        super(BugReport,self).__init__()
        uic.loadUi(f"files{os.sep}resources{os.sep}ui{os.sep}bugreport.ui",self)
        self.email = self.findChild(QLineEdit, "email")
        self.message = self.findChild(QTextEdit,"message")
        self.data = {}
    def showDialog(self):
        self.show()


    def send_email(self):
        #Sending your bug report via an API that I developed for secure communication and spam prevention

        if "@" in self.email:
            #sened message
            self.data['email'] = self.email
            self.data['message'] = self.message

            #sender = requests.Request('POST',URL, data = self.data)
            pass
        else:
            #complain about it
            pass
        pass

application = QApplication(sys.argv)
ui = BugReport()