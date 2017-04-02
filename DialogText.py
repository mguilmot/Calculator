# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\DialogText.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DialogText(object):
    def setupUi(self, DialogText):
        DialogText.setObjectName("DialogText")
        DialogText.resize(481, 281)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DialogText.setWindowIcon(icon)
        self.textBrowser = QtWidgets.QTextBrowser(DialogText)
        self.textBrowser.setGeometry(QtCore.QRect(20, 16, 441, 249))
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(DialogText)
        QtCore.QMetaObject.connectSlotsByName(DialogText)

    def retranslateUi(self, DialogText):
        _translate = QtCore.QCoreApplication.translate
        DialogText.setWindowTitle(_translate("DialogText", "DialogText"))
        self.textBrowser.setHtml(_translate("DialogText", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Hier komt de tekst.</p></body></html>"))

