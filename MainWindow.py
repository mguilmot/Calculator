# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(210, 308)
        MainWindow.setMinimumSize(QtCore.QSize(210, 308))
        MainWindow.setMaximumSize(QtCore.QSize(210, 308))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButtonPlus = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonPlus.setGeometry(QtCore.QRect(148, 228, 40, 40))
        self.pushButtonPlus.setObjectName("pushButtonPlus")
        self.labelResult = QtWidgets.QLabel(self.centralwidget)
        self.labelResult.setGeometry(QtCore.QRect(70, 10, 115, 33))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.labelResult.setFont(font)
        self.labelResult.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelResult.setObjectName("labelResult")
        self.labelInput = QtWidgets.QLabel(self.centralwidget)
        self.labelInput.setGeometry(QtCore.QRect(64, 52, 121, 19))
        self.labelInput.setText("")
        self.labelInput.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelInput.setObjectName("labelInput")
        self.pushButtonEqual = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonEqual.setGeometry(QtCore.QRect(104, 228, 40, 40))
        self.pushButtonEqual.setObjectName("pushButtonEqual")
        self.pushButtonComma = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonComma.setGeometry(QtCore.QRect(60, 228, 40, 40))
        self.pushButtonComma.setObjectName("pushButtonComma")
        self.pushButton0 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton0.setGeometry(QtCore.QRect(16, 228, 40, 40))
        self.pushButton0.setObjectName("pushButton0")
        self.pushButtonMinus = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonMinus.setGeometry(QtCore.QRect(148, 182, 40, 40))
        self.pushButtonMinus.setObjectName("pushButtonMinus")
        self.pushButton3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton3.setGeometry(QtCore.QRect(104, 182, 40, 40))
        self.pushButton3.setObjectName("pushButton3")
        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(60, 182, 40, 40))
        self.pushButton2.setObjectName("pushButton2")
        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(16, 182, 40, 40))
        self.pushButton1.setObjectName("pushButton1")
        self.pushButtonMultiply = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonMultiply.setGeometry(QtCore.QRect(148, 134, 40, 40))
        self.pushButtonMultiply.setObjectName("pushButtonMultiply")
        self.pushButton6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton6.setGeometry(QtCore.QRect(104, 134, 40, 40))
        self.pushButton6.setObjectName("pushButton6")
        self.pushButton5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton5.setGeometry(QtCore.QRect(60, 134, 40, 40))
        self.pushButton5.setObjectName("pushButton5")
        self.pushButton4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton4.setGeometry(QtCore.QRect(16, 134, 40, 40))
        self.pushButton4.setObjectName("pushButton4")
        self.pushButtonDevide = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonDevide.setGeometry(QtCore.QRect(148, 90, 40, 40))
        self.pushButtonDevide.setObjectName("pushButtonDevide")
        self.pushButton9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton9.setGeometry(QtCore.QRect(104, 90, 40, 40))
        self.pushButton9.setObjectName("pushButton9")
        self.pushButton8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton8.setGeometry(QtCore.QRect(60, 90, 40, 40))
        self.pushButton8.setObjectName("pushButton8")
        self.pushButton7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton7.setGeometry(QtCore.QRect(16, 90, 40, 40))
        self.pushButton7.setObjectName("pushButton7")
        self.pushButtonCE = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonCE.setGeometry(QtCore.QRect(16, 42, 40, 40))
        self.pushButtonCE.setObjectName("pushButtonCE")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 210, 21))
        self.menubar.setObjectName("menubar")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.actionREADME = QtWidgets.QAction(MainWindow)
        self.actionREADME.setObjectName("actionREADME")
        self.actionLICENSE = QtWidgets.QAction(MainWindow)
        self.actionLICENSE.setObjectName("actionLICENSE")
        self.menuAbout.addAction(self.actionREADME)
        self.menuAbout.addAction(self.actionLICENSE)
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator 1.0"))
        self.pushButtonPlus.setText(_translate("MainWindow", "+"))
        self.labelResult.setText(_translate("MainWindow", "0"))
        self.pushButtonEqual.setText(_translate("MainWindow", "="))
        self.pushButtonComma.setText(_translate("MainWindow", ","))
        self.pushButton0.setText(_translate("MainWindow", "0"))
        self.pushButtonMinus.setText(_translate("MainWindow", "-"))
        self.pushButton3.setText(_translate("MainWindow", "3"))
        self.pushButton2.setText(_translate("MainWindow", "2"))
        self.pushButton1.setText(_translate("MainWindow", "1"))
        self.pushButtonMultiply.setText(_translate("MainWindow", "X"))
        self.pushButton6.setText(_translate("MainWindow", "6"))
        self.pushButton5.setText(_translate("MainWindow", "5"))
        self.pushButton4.setText(_translate("MainWindow", "4"))
        self.pushButtonDevide.setText(_translate("MainWindow", ":"))
        self.pushButton9.setText(_translate("MainWindow", "9"))
        self.pushButton8.setText(_translate("MainWindow", "8"))
        self.pushButton7.setText(_translate("MainWindow", "7"))
        self.pushButtonCE.setText(_translate("MainWindow", "CE"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionREADME.setText(_translate("MainWindow", "README"))
        self.actionLICENSE.setText(_translate("MainWindow", "LICENSE"))

