import PyQt5
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QDialog, QLineEdit
from PyQt5 import uic
from files.resources.icons import icons
from subprocess import PIPE,Popen
import os
import sys



class BackupWindow(QDialog):

    def __init__(self):
        super(BackupWindow,self).__init__()
        uic.loadUi(f"files{os.sep}resources{os.sep}ui{os.sep}backup.ui",self)

        try:
            with open(f"files{os.sep}resources{os.sep}.config{os.sep}.pswd","r") as content:
                self.auth = content.read()
        except FileNotFoundError:
            pass


    def show_window(self):
        self.show()


    def take_backup(self):

        try:
            p = Popen(['sudo','-S'] + ['zip -r /usr/share/fonts_backup.zip /usr/share/fonts'], stdin = PIPE, stderr = PIPE, universal_newlines = True)
            su = p.communicate(self.auth + '\n')[0]

            p = Popen(['sudo','-S'] + [f'pc /usr/share/fonts_backup.zip files{os.sep}resources{os.sep}backup'], stdin = PIPE, stderr = PIPE, universal_newlines = True)
            su = p.communicate(self.auth + '\n')[0]
        except Exception as error:
            print("Error:",error)




application = QApplication(sys.argv)
ui = BackupWindow()