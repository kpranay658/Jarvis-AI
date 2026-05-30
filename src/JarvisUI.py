from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1301, 743)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.BG_1 = QtWidgets.QLabel(self.centralwidget)
        self.BG_1.setGeometry(QtCore.QRect(0, 0, 1301, 721))
        self.BG_1.setText("")
        self.BG_1.setPixmap(QtGui.QPixmap("64051853_f4014e.jpg"))
        self.BG_1.setScaledContents(True)
        self.BG_1.setObjectName("BG_1")

        self.Gif_1 = QtWidgets.QLabel(self.centralwidget)
        self.Gif_1.setGeometry(QtCore.QRect(420, 190, 511, 341))
        self.Gif_1.setText("")
        self.Gif_1.setPixmap(QtGui.QPixmap("Siri_1.gif"))
        self.Gif_1.setScaledContents(True)
        self.Gif_1.setObjectName("Gif_1")

        self.Gif_2 = QtWidgets.QLabel(self.centralwidget)
        self.Gif_2.setGeometry(QtCore.QRect(530, 430, 291, 151))
        self.Gif_2.setText("")
        self.Gif_2.setPixmap(QtGui.QPixmap("initial.gif"))
        self.Gif_2.setScaledContents(True)
        self.Gif_2.setObjectName("Gif_2")
        
        self.pushButton_start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_start.setGeometry(QtCore.QRect(40, 650, 93, 28))
        self.pushButton_start.setObjectName("pushButton_start")

        self.pushButton_Exist = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Exist.setGeometry(QtCore.QRect(1180, 650, 93, 28))
        self.pushButton_Exist.setObjectName("pushButton_Exist")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_start.setText(_translate("MainWindow", "START"))
        self.pushButton_Exist.setText(_translate("MainWindow", "EXIT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
