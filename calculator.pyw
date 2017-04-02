'''
    Basic python calculator
'''

import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from MainWindow import Ui_MainWindow
from DialogText import Ui_DialogText

class runApplication(Ui_MainWindow):
    def __init__(self):
        self.calcstr=""
        self.solution=0
        self.run()
        self.Quit()
        
    def run(self):
        self.app=QApplication(sys.argv)
        self.window=QMainWindow()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.buttonactions()
        self.menuactions()
        self.window.show()
        self.Quit()
        
    def buttonactions(self):
        self.ui.pushButton0.clicked.connect(lambda: self.Pushed('0'))
        self.ui.pushButton1.clicked.connect(lambda: self.Pushed('1'))
        self.ui.pushButton2.clicked.connect(lambda: self.Pushed('2'))
        self.ui.pushButton3.clicked.connect(lambda: self.Pushed('3'))
        self.ui.pushButton4.clicked.connect(lambda: self.Pushed('4'))
        self.ui.pushButton5.clicked.connect(lambda: self.Pushed('5'))
        self.ui.pushButton6.clicked.connect(lambda: self.Pushed('6'))
        self.ui.pushButton7.clicked.connect(lambda: self.Pushed('7'))
        self.ui.pushButton8.clicked.connect(lambda: self.Pushed('8'))
        self.ui.pushButton9.clicked.connect(lambda: self.Pushed('9'))
        self.ui.pushButtonPlus.clicked.connect(lambda: self.Pushed('+'))
        self.ui.pushButtonMinus.clicked.connect(lambda: self.Pushed('-'))
        self.ui.pushButtonMultiply.clicked.connect(lambda: self.Pushed('*'))
        self.ui.pushButtonDevide.clicked.connect(lambda: self.Pushed('/'))
        self.ui.pushButtonEqual.clicked.connect(lambda: self.Pushed('='))
        self.ui.pushButtonComma.clicked.connect(lambda: self.Pushed('.'))
        self.ui.pushButtonCE.clicked.connect(lambda: self.Pushed('CE'))
        
    def menuactions(self):
        self.ui.actionREADME.triggered.connect(lambda:self.openDialog('README'))
        self.ui.actionLICENSE.triggered.connect(lambda:self.openDialog('LICENSE'))
    
    def openDialog(self,filename):
        self.title=filename
        self.f=open(self.title+".txt")
        self.text=self.f.read()
        self.f.close()
        self.diag=runDialog(self.title,self.text)
        self.diag.show()
    
    def Pushed(self,strPushed):
        if strPushed=="=":
            self.calculation()
        elif strPushed=="CE":
            self.calcstr=""
            self.solution=0
            self.ui.labelResult.setText(str(self.solution))
            self.ui.labelInput.setText(str(self.solution))
        else:
            self.calcstr+=strPushed
            self.ui.labelInput.setText(str(self.calcstr))
    
    def calculation(self):
        if self.calcstr!="":
            self.solution=eval(self.calcstr)
            self.ui.labelResult.setText(str(self.solution))
            self.ui.labelInput.setText(str(self.solution))
            self.calcstr=str(self.solution)
    
    def Quit(self):
        sys.exit(self.app.exec_())

class runDialog(Ui_DialogText):
    def __init__(self,title,text):
        self.text=text
        self.title=title
        self.run()
    
    def run(self):
        self.window=QDialog()
        self.ui=Ui_DialogText()
        self.ui.setupUi(self.window)
        self.setText()

    def setText(self):
        self.window.setWindowTitle(self.title)
        self.ui.textBrowser.setPlainText(self.text)
    
    def show(self):
        self.window.show()

if __name__=="__main__":
    runApplication()
