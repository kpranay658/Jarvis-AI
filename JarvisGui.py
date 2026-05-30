import typing
from JarvisUI import Ui_MainWindow
from PyQt5 import QtCore , QtGui , QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtCore import QThread, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt , QTime , QTimer , QDate
from PyQt5.uic import loadUiType
import jarvis
import sys


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        jarvis.MainExecution3()


startExe = MainThread()


class Gui_start(QMainWindow):
    def __init__(self):
        super().__init__()

        self.gui = Ui_MainWindow()
        self.gui.setupUi(self)

        self.gui.pushButton_start.clicked.connect(self.startTask)
        self.gui.pushButton_Exist.clicked.connect(self.close) 

    def startTask(self):
       
        self.gui.label1 = QtGui.QMovie("Siri_1.gif")
        self.gui.Gif_1.setMovie(self.gui.label1)
        self.gui.label1.start()

        self.gui.label2 = QtGui.QMovie("initial.gif")
        self.gui.Gif_2.setMovie(self.gui.label2)
        self.gui.label2.start()

        startExe.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    jarvis_gui = Gui_start()
    jarvis_gui.show()
    sys.exit(app.exec_())

