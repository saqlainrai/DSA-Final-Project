
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QFileDialog
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5 import QtCore, QtWidgets
from PyQt5.uic import loadUi
from functools import partial
import pandas as pd
import csv

# from algorithms import *
# from Capital_Algos import *

df = pd.read_csv('customerData.csv')
dfMedicine = pd.read_csv('medicineData.csv')
dfOrders = pd.read_csv('ordersData.csv')

usernames = df['Name'].tolist()
emails = df['Email'].tolist()
contacts = df['Contact No.'].tolist()

class MainwindowDashboard(QMainWindow):
    def __init__(self, login_screen):
        self.log = login_screen
        super(MainwindowDashboard, self).__init__()
        loadUi("../ui/ui/Dashboard.ui",self)                 # Here we imported the QT Designer file which we made as Python GUI FIle.
        
        # Command to remove the default Windows Frame Design.
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        
        # Command to make the backgroud of Window transparent.
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        #These 2 lines are used to put funnctions on close and minimize buttons.
        # self.MinimizeButton.clicked.connect(lambda: self.showMinimized())
        
        self.btnClose.clicked.connect(lambda: self.close())                       #add cross(close) button
        self.btnExit.clicked.connect(self.displayLogin)                       #add cross(close) button
        self.btnHome.clicked.connect(partial(self.tableViewLoad, dfMedicine))
        self.btnCustomers.clicked.connect(partial(self.tableViewLoad, df))
        self.btnAOrders.clicked.connect(partial(self.tableViewLoad, dfOrders))
        
        # self.btnLogin.clicked.connect(self.login)

    def displayLogin(self):
        self.close()
        self.log.show()

    def tableViewLoad(self, data):
        self.model = QStandardItemModel()
        self.tableView.setModel(self.model)

        try:
            # data = pd.read_csv(path)
            self.model.setRowCount(data.shape[0])
            self.model.setColumnCount(data.shape[1])

            for col, header in enumerate(data.columns):
                header_item = QStandardItem(header)
                self.model.setHorizontalHeaderItem(col, header_item)

            for row in range(data.shape[0]):
                for col in range(data.shape[1]):
                    item = QStandardItem(str(data.iat[row, col]))
                    self.model.setItem(row, col, item)

            # Set color for horizontal header
            self.tableView.horizontalHeader().setStyleSheet("QHeaderView::section { background-color: lightblue; }")

            # Set color for vertical header
            self.tableView.verticalHeader().setStyleSheet("QHeaderView::section { background-color: lightblue; }")
        
        except Exception as e:
            print(f"Error loading data: {str(e)}")

class MainwindowSignUp(QMainWindow):
    def __init__(self, login_screen):
        self.log = login_screen
        super(MainwindowSignUp, self).__init__()
        loadUi("../ui/ui/SignUp.ui",self)                   # Here we imported the QT Designer file which we made as Python GUI FIle.
        
        # Command to remove the default Windows Frame Design.
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        
        # Command to make the backgroud of Window transparent.
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        #These 2 lines are used to put funnctions on close and minimize buttons.
        # self.MinimizeButton.clicked.connect(lambda: self.showMinimized())
        
        self.btnBack.clicked.connect(self.displayLogin)    
        self.btnSignUp.clicked.connect(self.signUp)      
        self.txtUsername.textChanged.connect(lambda: self.resetStyling(self.txtUsername))
        self.txtPassword.textChanged.connect(lambda: self.resetStyling(self.txtPassword))
        self.txtEmail.textChanged.connect(lambda: self.resetStyling(self.txtEmail))
        self.txtContact.textChanged.connect(lambda: self.resetStyling(self.txtContact))
        self.comboLocation.currentIndexChanged.connect(lambda: self.resetCombo(self.comboLocation)) 
        # self.btnLogin.clicked.connect(self.login)
    
    def resetCombo(self, obj):
        obj.setStyleSheet("background-color: #cdb4db;\nborder: 2px solid #555555;\ncolor:rgba(0,0,0,240);")
    def resetStyling(self, obj):
        obj.setStyleSheet("border: 2px solid #555555;\nbackground-color:rgba(0,0,0,0);\nborder-bottom:2px solid rgba(46,82,101,200);\ncolor:rgba(0,0,0,240);\npadding-bottom:0px;	")

    def displayLogin(self):
        self.close()
        self.log.show()

    def findExistingUser(self, name, email, contact):
        for i in range(len(usernames)):
            if usernames[i] == name and emails[i] == email and contacts[i] == contact:
                return True
        return False

    def signUp(self):
        global df                           # to show it is global
        name = self.txtName.text()
        Fname = self.txtFName.text()
        username = self.txtUsername.text()
        password = self.txtPassword.text()
        cnic = self.txtCNIC.text()
        email = self.txtEmail.text()
        contact = self.txtContact.text()
        location = self.comboLocation.currentText()
        
        confirmation = self.confirmData(username, password, email, contact, location)
        flag = self.findExistingUser(username, email, contact)
        if confirmation:                                       # user not exists
            if not flag:
                self.txtName.clear()
                self.txtFName.clear()
                self.txtUsername.clear()
                self.txtPassword.clear()
                self.txtCNIC.clear()
                self.txtEmail.clear()
                self.txtContact.clear()
                self.comboLocation.setCurrentIndex(0)
                new_row = {'Name': name, 'Father Name': Fname, 'Username': username, 'Password': password, 'CNIC': cnic, 'Email': email, 'Contact No.': contact, 'Location': location}
                df = df._append(new_row, ignore_index=True)
                
                df.to_csv('customerData.csv', index=False)

                self.comments.setText("User Registered Successfully!!!")
            else:
                self.comments.setText("User already exists. Try Again!!!")

    def confirmData(self, username, password, email, contact, location):
        # if username == "" or password == "" or email == "" or contact == "":
        if username != "":
            if password != "":
                if email.endswith("@gmail.com"):
                    if contact != "":
                        if location != "---Select Location---*":
                            return True
                        else:
                            self.comments.setText("Add valid Location!!!")
                            self.comboLocation.setStyleSheet("border: 2px solid red;")
                    else:
                        self.comments.setText("Add valid Contact No.!!!")
                        self.txtContact.setStyleSheet("border: 2px solid red;")
                else:
                    self.comments.setText("Add valid Email!!!")
                    self.txtEmail.setStyleSheet("border: 2px solid red;")
            else:
                self.comments.setText("Add valid Password!!!")
                self.txtPassword.setStyleSheet("border: 2px solid red;")
        else:
            self.comments.setText("Add valid Username!!!")
            self.txtUsername.setStyleSheet("border: 2px solid red;")
        return False

# def main():
#         import sys
#         app = QtWidgets.QApplication(sys.argv)
#         # MainWindow = QtWidgets.QMainWindow()
#         window = MainwindowDashboard()
#         window.show()
#         sys.exit(app.exec_())

# if __name__ == "__main__":
#         main()
