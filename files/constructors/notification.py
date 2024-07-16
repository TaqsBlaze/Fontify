import PyQt5
from PyQt5.QtWidgets import QLabel, QPushButton, QApplication, QWidget, QMainWindow, QDialog, QLineEdit
from files.constructors import configure
from PyQt5 import uic
import os
import sys




class Notification(QDialog):

    def __init__(self):
        super(Notification, self).__init__()
        uic.loadUi(f"files{os.sep}resources{os.sep}ui{os.sep}notifications.ui",self)
        self.message = self.findChild(QLabel, "messageLabel")
        self.ok_button = self.findChild(QPushButton, "okButton")
        # self.message.setText('')
        self.ok_button.clicked.connect(self.open_password_config)
        self.message.setStyleSheet("font-size: 10pt")
        try:
            with open(f"files{os.sep}.notif","r") as content:
                notif = content.read()

                self.message.setText(notif)
                os.system(f"rm files{os.sep}.notif")
        except FileNotFoundError:
            self.message.setText("System error: Notification source not found")
            pass 

    def open_password_config(self):

        configure.ui.show()
        self.destroy()



application = QApplication(sys.argv)
ui = Notification()