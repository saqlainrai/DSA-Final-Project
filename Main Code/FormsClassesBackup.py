
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QFileDialog
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5 import QtCore, QtWidgets
from PyQt5.uic import loadUi
from functools import partial
import pandas as pd
import csv

from datetime import datetime

from Algos.linearSearch import linearSearch
from Algos.BubleSort import bubble_sort
from Algos.InsertionSort import insertion_sort
from Algos.SelectionSort import SelectionSort
from Algos.ShellSort import shellSort


# from algorithms import *
# from Capital_Algos import *

medicinePath = "data.csv"
df = pd.read_csv('customerData.csv')
dfMedicine = pd.read_csv(medicinePath)
dfOrders = pd.read_csv('ordersData.csv')
dfPrevious = pd.read_csv('previousOrders.csv')

usernames = df['Username'].tolist()
passes = df['Password'].tolist()
emails = df['Email'].tolist()
contacts = df['Contact No.'].tolist()
locations = df['Location'].tolist()

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

class MainwindowDetails(QMainWindow):
    def __init__(self, mainDashboard, index):
        self.userIndex = index
        self.log = mainDashboard
        super(MainwindowDetails, self).__init__()
        loadUi("../ui/ui/details.ui",self)                   # Here we imported the QT Designer file which we made as Python GUI FIle.
        self.btnUpdate.setEnabled(False)

        # Command to remove the default Windows Frame Design.
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        
        # Command to make the backgroud of Window transparent.
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        #These 2 lines are used to put funnctions on close and minimize buttons.
        # self.MinimizeButton.clicked.connect(lambda: self.showMinimized())
        
        usernames = df['Username'].tolist()
        emails = df['Email'].tolist()
        contacts = df['Contact No.'].tolist()
        names = df['Name'].tolist()
        fnames = df['Father Name'].tolist()
        cnic = df['CNIC'].tolist()
        location = df['Location'].tolist()
        passes = df['Password'].tolist()

        self.txtName.setText(str(names[self.userIndex]))
        self.txtFName.setText(str(fnames[self.userIndex]))
        self.txtUsername.setText(str(usernames[self.userIndex]))
        self.txtPassword.setText(str(passes[self.userIndex]))
        self.txtCNIC.setText(str(cnic[self.userIndex]))
        self.txtEmail.setText(str(emails[self.userIndex]))
        self.txtContact.setText(str(contacts[self.userIndex]))
        self.comboLocation.setCurrentText(str(location[self.userIndex]))

        self.btnBack.clicked.connect(self.displayLogin)    
        self.btnUpdate.clicked.connect(self.update)      
        self.txtUsername.textChanged.connect(lambda: self.resetStyling(self.txtUsername))
        self.txtPassword.textChanged.connect(lambda: self.resetStyling(self.txtPassword))
        self.txtEmail.textChanged.connect(lambda: self.resetStyling(self.txtEmail))
        self.txtContact.textChanged.connect(lambda: self.resetStyling(self.txtContact))
        self.comboLocation.currentIndexChanged.connect(lambda: self.resetCombo(self.comboLocation)) 
        # self.btnLogin.clicked.connect(self.login)
    
    def resetCombo(self, obj):
        self.btnUpdate.setEnabled(True)
        obj.setStyleSheet("background-color: #cdb4db;\nborder: 2px solid #555555;\ncolor:rgba(0,0,0,240);")
    def resetStyling(self, obj):
        self.btnUpdate.setEnabled(True)
        obj.setStyleSheet("border: 2px solid #555555;\nbackground-color:rgba(0,0,0,0);\nborder-bottom:2px solid rgba(46,82,101,200);\ncolor:rgba(0,0,0,240);\npadding-bottom:0px;	")

    def displayLogin(self):
        self.close()
        self.log.show()

    def findExistingUser(self, name, email, contact):
        for i in range(len(usernames)):
            if usernames[i] == name and emails[i] == email and contacts[i] == contact:
                return True
        return False

    def update(self):
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
                # self.txtName.clear()
                # self.txtFName.clear()
                # self.txtUsername.clear()
                # self.txtPassword.clear()
                # self.txtCNIC.clear()
                # self.txtEmail.clear()
                # self.txtContact.clear()
                # self.comboLocation.setCurrentIndex(0)
                new_row = {'Name': name, 'Father Name': Fname, 'Username': username, 'Password': password, 'CNIC': cnic, 'Email': email, 'Contact No.': contact, 'Location': location}
                df.loc[self.userIndex] = new_row
                df.to_csv('customerData.csv', index=False)
                self.btnUpdate.setEnabled(False)
                self.comments.setText("Details updated successfully")
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

class MainWindowUser(QMainWindow):
    def __init__(self, user):
        self.userIndex = user.index
        self.log = user.loginScreen
        self.currentDataFrame = None
        super(MainWindowUser, self).__init__()
        loadUi("../ui/ui/User.ui",self)                 # Here we imported the QT Designer file which we made as Python GUI FIle.
        # self.tableView.hideTableView()
        self.tableFrameBoth.setVisible(False)
        self.setProperties()                            # set the values and stylesheets of content
        
        # Command to remove the default Windows Frame Design.
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        
        # Command to make the backgroud of Window transparent.
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        #These 2 lines are used to put funnctions on close and minimize buttons.
        # self.MinimizeButton.clicked.connect(lambda: self.showMinimized())
        
        self.btnClose.clicked.connect(lambda: self.close())                       #add cross(close) button
        self.btnExit.clicked.connect(self.displayLogin)                       #add cross(close) button
        self.btnHome.clicked.connect(self.homePressed)
        self.btnStock.clicked.connect(self.stockPressed)
        self.btnAOrders.clicked.connect(self.AOrdersPressed)
        self.btnPOrders.clicked.connect(self.POrdersPressed)
        self.btnSetting.clicked.connect(self.settingPressed)
        self.btnOrder.clicked.connect(self.orderPressed)
        self.btnSearch.clicked.connect(self.searchPressed)
        # self.btnLogin.clicked.connect(self.login)
    
    def searchPressed(self):
        query = self.txtSearch.text()
        colIndex = self.comboColumns.currentIndex()
        if query == "":
            self.labelComments.setText("Enter a valid query....")
        else:
            data = self.currentDataFrame.values.tolist()
            sameUsers = linearSearch(data, query, colIndex)
            name, price, discount, manufacturer, type, size, cmp1, cmp2 = [], [], [], [], [], [], [], []
            for i in sameUsers:
                name.append(i[0])
                price.append(i[1])
                discount.append(i[2])
                manufacturer.append(i[3])
                type.append(i[4])
                size.append(i[5])
                cmp1.append(i[6])
                cmp2.append(i[7])
            data = {'Name': name,
                    'Price': price,
                    'Discount': discount,
                    'Manufacturer': manufacturer,
                    'Type': type,
                    'Composition1': cmp1,
                    'Composition2': cmp2}
            temp = pd.DataFrame(data)
            self.tableViewLoad(temp)
            self.currentDataFrame = temp

    def orderPressed(self):
        count = self.spinQuantity.value()
        if self.tableView.currentIndex().row() != -1 and count > 0:
            self.labelComments.setText("Enjoy the best version of Program")
            index = self.tableView.selectedIndexes()[0].row()
            array = self.currentDataFrame.values.tolist()

            # Append the new data
            price = array[index][1]
            total = price * count
            
            current_datetime = datetime.now()
            current_date = current_datetime.date()
            original_date = datetime.strptime(str(current_date), "%Y-%m-%d")
            current_date = original_date.strftime("%d/%m/%Y")
            
            new_data = {'Name':usernames[self.userIndex], 'Password':passes[self.userIndex],'Location':locations[self.userIndex],'Product':array[index][0],'Quantity': count,'Price':price,'Total Bill':total,'Due Data':current_date}
            df2 = dfOrders._append(new_data, ignore_index=True)
            df2.to_csv('ordersData.csv', index=False)
            print("Data added to ordersData.csv")
        else:
            self.labelComments.setText("Select valid Arguments")

    def setProperties(self):
        msg = f"Welcome, {usernames[self.userIndex]}"
        self.greet.setText(msg)
        self.tableFrameBoth.setStyleSheet("")
        self.greetFrame.move(30, 70)

    def homePressed(self):
        self.greetFrame.show()
        self.tableFrameBoth.setVisible(False)
    
    def stockPressed(self):
        self.greetFrame.hide()
        self.tableViewLoad(dfMedicine)
        self.currentDataFrame = dfMedicine
        self.tableFrameBoth.setVisible(True)
        self.addToComboBox(self.comboColumns, self.getCsvHeader(medicinePath))
        self.addToComboBox(self.comboColumns2, self.getCsvHeader(medicinePath))
        self.comboColumns.setCurrentIndex(0)
        self.comboColumns2.setCurrentIndex(0)
        self.btnSort.clicked.connect(self.sortPressed)

    def sortPressed(self):
        criteria = None
        algo = self.comboAlgos.currentText()
        colIndex = self.comboColumns2.currentIndex()
        
        if self.radioAsc.isChecked() or self.radioDes.isChecked():
            criteria = self.radioAsc.isChecked()
        array = self.currentDataFrame.values.tolist()  
        if algo != "---Select an Algorithm---" and criteria != None:
            if algo == "Bubble Sort":
                bubble_sort(array, colIndex, criteria)
            elif algo == "Insertion Sort":
                insertion_sort(array, colIndex, criteria)
            name, price, discount, manufacturer, type, size, cmp1, cmp2 = [], [], [], [], [], [], [], []
            for i in array:
                name.append(i[0])
                price.append(i[1])
                discount.append(i[2])
                manufacturer.append(i[3])
                type.append(i[4])
                size.append(i[5])
                cmp1.append(i[6])
                cmp2.append(i[7])
            data = {'Name': name,
                'Price': price,
                'Discount': discount,
                'Manufacturer': manufacturer,
                'Type': type,
                'Composition1': cmp1,
                'Composition2': cmp2}
            temp = pd.DataFrame(data)
            self.tableViewLoad(temp)
            self.currentDataFrame = temp
        else:
            self.labelComments.setText("Select the valid Queries!!!")

    def AOrdersPressed(self):
        self.greetFrame.hide()
        data = dfOrders.values.tolist()
        sameUsers = linearSearch(data, str(usernames[self.userIndex]), 0)
        final = linearSearch(sameUsers, str(passes[self.userIndex]), 1) 
        product, quantity, price, total, location, date = [], [], [], [], [], []
        for i in final:
            product.append(i[3])
            quantity.append(i[4])
            price.append(i[5])
            total.append(i[6])
            location.append(i[2])
            date.append(i[7])
        data = {'Product': product,
                'Quantity': quantity,
                'Price': price,
                'Total Bill': total,
                'Location': location,
                'Date': date}
        temp = pd.DataFrame(data)
        self.currentDataFrame = temp
        self.tableViewLoad(temp)
        # self.tableFrameSort.setVisible(True)
        self.tableFrameBoth.setVisible(False)
        
        header = self.currentDataFrame.columns.tolist()
        self.addToComboBox(self.comboColumns, header)
        self.addToComboBox(self.comboColumns2, header)
        self.comboColumns.setCurrentIndex(0)
        self.comboColumns2.setCurrentIndex(0)
    
    def POrdersPressed(self):
        self.greetFrame.hide()
        
        data = dfPrevious.values.tolist()
        sameUsers = linearSearch(data, str(usernames[self.userIndex]), 0)
        final = linearSearch(sameUsers, str(passes[self.userIndex]), 1) 
        product, quantity, price, total, location, date = [], [], [], [], [], []
        for i in final:
            product.append(i[3])
            quantity.append(i[4])
            price.append(i[5])
            total.append(i[6])
            location.append(i[2])
            date.append(i[7])
        data = {'Product': product,
                'Quantity': quantity,
                'Price': price,
                'Total Bill': total,
                'Location': location,
                'Date': date}
        temp = pd.DataFrame(data)

        self.tableViewLoad(temp)
        self.currentDataFrame = temp
        # self.tableFrameSort.setVisible(True)
        self.tableFrameBoth.setVisible(False)

        header = self.currentDataFrame.columns.tolist()
        self.addToComboBox(self.comboColumns, header)
        self.addToComboBox(self.comboColumns2, header)
        self.comboColumns.setCurrentIndex(0)
        self.comboColumns2.setCurrentIndex(0)
    
    def settingPressed(self):
        self.greetFrame.hide()
        self.displayDetails()
        self.tableFrame.setVisible(False)
    
    def displayDetails(self):
        self.hide()                     # Hide the current window
        # Create and show a new window
        new_window = MainwindowDetails(self, self.userIndex)
        new_window.show()

    def addToComboBox(self, obj, data):
        obj.clear()
        for i in data:
            obj.addItem(i)

    def getCsvHeader(self, file_path):
        df = pd.read_csv(file_path, nrows=0)  # Read only the first row (header)
        header = df.columns.tolist()
        return header

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
