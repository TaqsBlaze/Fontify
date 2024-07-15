import PyQt5
from PyQt5.QtWidgets import QLabel, QFileDialog, QPushButton, QApplication, QWidget, QMainWindow, QFrame, QLineEdit
from PyQt5.QtGui import QFont, QFontDatabase
from PyQt5 import uic
from PyQt5.QtCore import QUrl
from files.constructors import about
from files.constructors import bugreport
from files.constructors import backup
from files.constructors import notification
from files.resources.icons import icons
from subprocess import Popen, PIPE
import sys
import os




class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow,self).__init__()
        uic.loadUi(f"files{os.sep}resources{os.sep}ui{os.sep}main.ui",self)
        self.actionReport_Bug.triggered.connect(self.bug_report)
        self.actionBackup.triggered.connect(self.backup_window)
        self.font_suply = self.findChild(QLineEdit, "fontInput")
        self.install = self.findChild(QPushButton, "installButton")
        self.brows_fonts = self.findChild(QPushButton,"openDialog")
        self.message = self.findChild(QLabel, "messageLabel")
        self.message.setText('')
        self.brows_fonts.clicked.connect(self.get_font)
        self.install.clicked.connect(self.install_font)

        self.display1 = self.findChild(QLabel, "display1")
        self.display2 = self.findChild(QLabel, "display2")
        self.display3 = self.findChild(QLabel, "display3")

        self.displays = [self.display1,self.display2,self.display3]

        try:
            #setting sudo password
            with open(f"files{os.sep}resources{os.sep}.config{os.sep}.pswd","r") as content:
                self.auth = content.read()
        except FileNotFoundError:
            with open(f"files{os.sep}.notif","w") as content:
                content.write("You need to configure your password first!\nClick Ok to configure your password")
            
            notification.ui.show()

            # pass

    def bug_report(self):
        #Send a bug report
        bugreport.ui.show()
        pass

    def backup_window(self):
        #Backup system font
        backup.ui.show()

    def install_font(self):
        #installing font into system fonts
        pass

    def get_font(self):
        #File dialog for opening font file location
        open_dir =  os.path.expanduser('~') + f"{os.sep}Downloads"
        font_url = QFileDialog.getOpenFileUrl(self, 'Open Font file',QUrl(open_dir),"Font files (*.ttf)")[0].toLocalFile()
        self.font_suply.setText(font_url)
        font_id = QFontDatabase.addApplicationFont(font_url)
        font_name = QFontDatabase.applicationFontFamilies(font_id)[0]
        font = QFont(font_name)

        font_sizes = "21pt 30pt 48pt".split()
        index = 0
        for display in self.displays:
            display.setFont(font)
            display.setStyleSheet(f"font-size: {font_sizes[index]}")
            if index == 1:
                display.setStyleSheet(f"font-size: {font_sizes[index]}; font: italic")

            elif index == 3:
                display.setStyleSheet(f"font-size: {font_sizes[index]}; bold")
            index += 1

        print(font_url)

    def install_font(self):
        #Installing font

        if self.font_suply.text() != '':

            try:
                install = Popen(['sudo','-S'] + f"cp {self.font_suply.text()} /usr/share/fonts/truetype".split(), stdin = PIPE, stderr = PIPE, universal_newlines = True)
                exc = install.communicate(self.auth + '\n')[0]
                refresh = Popen(['sudo','-S'] + 'fc-cache'.split(), stdin= PIPE, stderr = PIPE, universal_newlines = True)
                xcc = refresh.communicate(self.auth + '\n')
                self.message.setText("Font was installed successfully..")
                self.message.setStyleSheet("color:green")
            except Exception as error:
                self.message.setText(f"Failed to install font \n{error}")
                self.message.setStyleSheet("color:red")

                #revert incase user retries
                if self.font_suply.text() != '':
                    if os.path.isfile(f"/usr/share/fonts/truetype/{self.font_suply.text().split('/')[-1]}"):
                        remove = Popen(['sudo','-S'] + f"rm /usr/share/fonts/truetype/{self.font_suply.text().split('/')[-1]}".split(),
                                       stderr= PIPE, stdin= PIPE, universal_newlines= True)
                        exc = remove.communicate(self.auth)[0]

        else:
            self.message.setText("Font can not be empty\n Please provide a valid .ttf font file")
            self.message.setStyleSheet("color:red")



application = QApplication(sys.argv)
window = MainWindow()
window.show()
application.exec()
