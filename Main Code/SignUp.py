
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QFileDialog
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5 import QtCore, QtWidgets
from PyQt5.uic import loadUi
from functools import partial
import pandas as pd
import csv

df = pd.read_csv('customerData.csv')
dfMedicine = pd.read_csv('medicineData.csv')
dfOrders = pd.read_csv('ordersData.csv')

usernames = df['Name'].tolist()
emails = df['Email'].tolist()
contacts = df['Contact No.'].tolist()

class MainwindowSignUp(QMainWindow):
    def __init__(self, login_screen):
        print("Constructor Called")
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

        # self.btnLogin.clicked.connect(self.login)

    def displayLogin(self):
        self.close()
        self.log.show()

    def findExistingUser(name, email, contact):
        for i in range(len(usernames)):
            if usernames[i] == name and emails[i] == email and contacts[i] == contact:
                return True
        return False

    def signUp(self):
        name = self.txtName.text()
        Fname = self.txtFName.text()
        username = self.txtUsername.text()
        password = self.txtPassword.text()
        cnic = self.txtCNIC.text()
        email = self.txtEmail.text()
        contact = self.txtContact.text()
        location = self.comboLocation.currentIndex()
        
        flag = self.findExistingUser(username, email, contact)
        if not flag:                                       # user not exists
            self.txtName.clear()
            self.txtFName.clear()
            self.txtUsername.clear()
            self.txtPassword.clear()
            self.txtCNIC.clear()
            self.txtEmail.clear()
            self.txtContact.clear()
            self.comboLocation.setCurrentIndex(0)
            new_row = {'Name': name, 'Father Name': Fname, 'Username': username, 'Password': password, 'CNIC': cnic, 'Email': email, 'Contact No.': contact, 'Location': location}
            df = df.append(new_row, ignore_index=True)
            
            df.to_csv('your_file.csv', index=False)

            self.displayLogin()
        else:
            print("User already exists. Try Again!!!")

# def main():
#         import sys
#         app = QtWidgets.QApplication(sys.argv)
#         # MainWindow = QtWidgets.QMainWindow()
#         window = MainwindowDashboard()
#         window.show()
#         sys.exit(app.exec_())

# if __name__ == "__main__":
#         main()
