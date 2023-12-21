
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QFileDialog
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5 import QtCore, QtWidgets
from PyQt5.uic import loadUi
from functools import partial
import pandas as pd
import csv

from FormsClasses import *
from AdminDashboard import *

class UserDetails():
    def __init__(self, name, password, index):
        self.name = name
        self.password = password
        self.index = index
        self.loginScreen = None

class Mainwindow(QMainWindow):
    def __init__(self):
        self.userIndex = -1
        super(Mainwindow, self).__init__()
        loadUi("../ui/ui/SignIn.ui",self)                 # Here we imported the QT Designer file which we made as Python GUI FIle.
        
        # Command to remove the default Windows Frame Design.
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        
        # Command to make the backgroud of Window transparent.
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        #These 2 lines are used to put functions on close and minimize buttons.
        # self.MinimizeButton.clicked.connect(lambda: self.showMinimized())
        
        self.btnExit.clicked.connect(lambda: self.close())                       #add cross(close) button
        # self.btnSignIn.clicked.connect(self.loginScreen)
        # self.btnSignUp.clicked.connect(self.signUpScreen)

        self.btnSignIn.clicked.connect(self.tempScreen)
        
        # self.btnLogin.clicked.connect(self.login)

    def tempScreen(self):
        user = UserDetails('a', 'b', 4)
        user.loginScreen = self
        self.hide()                     # Hide the current window
        # Create and show a new window
        self.new_window = MainwindowDashboard(user)
        self.new_window.show()

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
        flag = self.validate(username, password)
        
        if username == "Saqlain" and password == "1234":
            user = UserDetails(username, password, -1)
            user.loginScreen = self
            self.hide()                     # Hide the current window
            # Create and show a new window
            new_window = MainwindowDashboard(user)
            new_window.show()
        else:
            if flag:
                user = UserDetails(username, password, self.userIndex)
                user.loginScreen = self
                self.hide()                     # Hide the current window
                # Create and show a new window
                new_window = MainWindowUser(user)
                new_window.show()
            else:
                self.comments.setText("User Not Found!!!")
    
    def validate(self, name, password):
        df = pd.read_csv('customerData.csv')
        names = df["Username"].tolist()
        passes = df["Password"].tolist()
        for i in range(len(names)):
            temp = Decrypt(passes[i])
            if name == names[i] and password == temp:
                self.userIndex = i
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
