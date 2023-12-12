
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QFileDialog
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5 import QtCore, QtWidgets
from PyQt5.uic import loadUi
from functools import partial
import pandas as pd
import csv

# from algorithms import *
# from Capital_Algos import *
from FormsClasses import *
# from SignUp import *

df = pd.read_csv('medicineData.csv')

class Mainwindow(QMainWindow):
    def __init__(self):
        super(Mainwindow, self).__init__()
        loadUi("../ui/ui/SignIn.ui",self)                 # Here we imported the QT Designer file which we made as Python GUI FIle.
        
        # Command to remove the default Windows Frame Design.
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        
        # Command to make the backgroud of Window transparent.
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        #These 2 lines are used to put functions on close and minimize buttons.
        # self.MinimizeButton.clicked.connect(lambda: self.showMinimized())
        
        self.btnExit.clicked.connect(lambda: self.close())                       #add cross(close) button
        self.btnSignIn.clicked.connect(self.loginScreen)
        self.btnSignUp.clicked.connect(self.signUpScreen)
        
        # self.btnLogin.clicked.connect(self.login)

    def signUpScreen(self):
        self.hide()                     # Close the current window
        # Create and show a new window
        self.new_window = MainwindowSignUp(self)
        self.new_window.show()

    def loginScreen(self):
        username = self.txtUsername.text()
        password = self.txtPassword.text()
        self.txtUsername.clear()
        self.txtPassword.clear()
        flag = validate(username, password)
        # if flag:
        self.hide()                     # Hide the current window
        # Create and show a new window
        new_window = MainwindowDashboard(self)
        new_window.show()
        # else:
            # pass                      # implement it

def validate(name, password):
    if name == "Saqlain" and password == "1234":
        return True
    else:
        return False

def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    # MainWindow = QtWidgets.QMainWindow()
    window = Mainwindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
