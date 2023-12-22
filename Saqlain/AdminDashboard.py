

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
from Algos.ShellSort import shellSort
from Algos.CountingSort import counting_sort
from Algos.mergeSort import merge_sort
from Algos.QuickSort import quick_sort
from Algos.SelectionSort import SelectionSort

from Algos.GraphDisplay import *
from FormsClasses import *

from classes import *
from Algos.queue import *
capital_Queue = queue()

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

graphDisplay = Graph()
graphCalculate = CityGraph()
add_edges(graphDisplay)
loadGraph(graphCalculate)

class MainwindowDashboard(QMainWindow):
    def __init__(self, userObject):
        self.user = userObject
        self.currentDataFrame = None
        self.medicines = None
        super(MainwindowDashboard, self).__init__()
        loadUi("../ui/ui/Dashboard.ui",self)                 # Here we imported the QT Designer file which we made as Python GUI FIle.
        self.icon.setVisible(True)
        self.frameSecond.setVisible(False)
        self.frameSecond.setStyleSheet("")
        
        # Command to remove the default Windows Frame Design.
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        
        # Command to make the backgroud of Window transparent.
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        #These 2 lines are used to put funnctions on close and minimize buttons.
        # self.MinimizeButton.clicked.connect(lambda: self.showMinimized())
        
        #-----------------Side bar buttons------------------------------
        self.btnClose.clicked.connect(lambda: self.close()) 
        self.btnExit.clicked.connect(self.displayLogin)     
        self.btnHome.clicked.connect(self.homePressed)
        self.btnMedicines.clicked.connect(self.displayMedicines)
        self.btnCustomers.clicked.connect(self.showCustomers)
        self.btnAOrders.clicked.connect(self.displayOrders)
        self.btnDOrders.clicked.connect(self.displayOrders)
        self.btnMap.clicked.connect(self.displayMap)
        
        #-----------------Other buttons------------------------------
        self.btnSearch.clicked.connect(self.searchPressed)
        self.btnSort.clicked.connect(self.sortPressed)
        self.btnRemove.clicked.connect(self.removePressed)
        self.btnAdd.clicked.connect(self.addPressed)

    def searchPressed(self):
        query = self.txtSearch.text()
        colIndex = self.comboColumns.currentIndex()
        if query != "":
            self.txtSearch.clear()
            df = self.currentDataFrame.values.tolist()
            data = linearSearch(df, query, colIndex)
            if self.medicines:
                temp = self.convertToDFMedicines(data)
            else:
                temp = self.convertToDFCustomers(data)
            self.tableViewLoad(temp)
        else:
            self.txtComments.setText("Please enter a valid query.")

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
            elif algo == "Selection Sort":
                SelectionSort(array, colIndex, criteria)
            elif algo == "Quick Sort":
                quick_sort(array, 0, len(array)-1, colIndex)
            elif algo == "Merge Sort":
                merge_sort(array, 0, len(array)-1, colIndex, criteria)
            elif algo == "Bucket Sort" or algo == "Counting Sort":
                if colIndex == -1:
                    counting_sort(array, colIndex)
                else:
                    self.txtComments.setText("Select a valid Column!!!")
            if self.medicines:
                temp = self.convertToDFMedicines(array)
            else:
                temp = self.convertToDFCustomers(array)
            self.tableViewLoad(temp)
            self.currentDataFrame = temp
        else:
            self.txtComments.setText("Select the valid Queries!!!")

    def removePressed(self):
        if self.medicines:
            if self.tableView.currentIndex().row() != -1:
                self.txtComments.setText("Enjoy the best version of Program")
                index = self.tableView.selectedIndexes()[0].row()
                array = self.currentDataFrame.values.tolist()

                #over-write that index
                for i in range(index, len(array)):
                    if i == len(array)-1:
                        array.pop()
                        continue
                    array[i] = array[i+1]
                
                df = self.convertToDFMedicines(array)

                df.to_csv('data.csv', index=False)
                self.currentDataFrame = df
                self.tableViewLoad(df)
                self.txtComments.setText("The Data is removed Successfully!!!")
            else:
                self.txtComments.setText("Select a row to remove it!!!")
        else:
            if self.tableView.currentIndex().row() != -1:
                self.txtComments.setText("Enjoy the best version of Program")
                index = self.tableView.selectedIndexes()[0].row()
                array = self.currentDataFrame.values.tolist()

                #over-write that index
                for i in range(index, len(array)):
                    if i == len(array)-1:
                        array.pop()
                        continue
                    array[i] = array[i+1]

                for i in range(len(array)):
                    array[i][3] = Encrypt(array[i][3])
                
                df = self.convertToDFCustomers(array)

                df.to_csv('customerData.csv', index=False)

                array = df.values.tolist()
                for i in range(len(array)):
                    array[i][3] = Decrypt(array[i][3])
                
                new_df = pd.DataFrame(array, columns=df.columns)
                self.currentDataFrame = new_df
                self.tableViewLoad(new_df)
                self.txtComments.setText("The Data is removed Successfully!!!")
            else:
                self.txtComments.setText("Select a row to remove it!!!")

    def addPressed(self):
        if self.medicines:
            window = windowAddMedicine(self)
            window.show()
        else:
            window = windowAddUser(self)
            window.show()

    def convertToDFCustomers(self, data):
        name, fname, username, password, cnic, email, contactNo, location = [], [], [], [], [], [], [], []
        for i in data:
            name.append(i[0])
            fname.append(i[1])
            username.append(i[2])
            password.append(i[3])
            cnic.append(i[4])
            email.append(i[5])
            contactNo.append(i[6])
            location.append(i[7])
        data = {'Name': name,
                'Father Name': fname,
                'Username': username,
                'Password': password,
                'CNIC': cnic,
                'Email': email,
                'Contact No.': contactNo,
                'Location': location}
        temp = pd.DataFrame(data)
        return temp

    def convertToDFMedicines(self, data):
        name, price, discount, manufacturer, type, size, cmp1, cmp2 = [], [], [], [], [], [], [], []
        for i in data:
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
                'Size': size,
                'Composition1': cmp1,
                'Composition2': cmp2}
        temp = pd.DataFrame(data)
        return temp

    def homePressed(self):
        self.frameSecond.setVisible(False)
        self.icon.setVisible(True)

    def displayMedicines(self):
        dfMedicine = pd.read_csv("data.csv")
        self.medicines = True
        self.icon.setVisible(False)
        self.addToComboBox(self.comboColumns, self.getCsvHeader(medicinePath))
        self.addToComboBox(self.comboColumns2, self.getCsvHeader(medicinePath))
        self.comboColumns.setCurrentIndex(0)
        self.comboColumns2.setCurrentIndex(0)
        self.currentDataFrame = dfMedicine
        self.tableViewLoad(dfMedicine)
        self.frameSecond.setVisible(True)

    def addToComboBox(self, obj, data):
        obj.clear()
        for i in data:
            obj.addItem(i)

    def getCsvHeader(self, file_path):
        df = pd.read_csv(file_path, nrows=0)
        header = df.columns.tolist()
        return header

    def displayOrders(self):
        self.hide()
        temp = self.user
        temp.loginScreen = self
        self.orders_window = MainwindowOrders(temp)
        self.orders_window.show()

    def showCustomers(self):
        df = pd.read_csv("customerData.csv")
        self.medicines = False
        self.icon.setVisible(False)
        self.addToComboBox(self.comboColumns, self.getCsvHeader("customerData.csv"))
        self.addToComboBox(self.comboColumns2, self.getCsvHeader("customerData.csv"))
        self.comboColumns.setCurrentIndex(0)
        self.comboColumns2.setCurrentIndex(0)

        data = df.values.tolist()
        for i in range(len(data)):
            data[i][3] = Decrypt(data[i][3])
        new_df = pd.DataFrame(data, columns=df.columns)
        self.tableViewLoad(new_df)
        self.currentDataFrame = new_df
        self.frameSecond.setVisible(True)
    
    def displayMap(self):
        self.hide()
        temp = self.user
        temp.loginScreen = self
        self.maps = MainwindowMaps(temp)
        self.maps.show()

    def displayLogin(self):
        self.close()
        self.user.loginScreen.show()

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

class MainwindowMaps(QMainWindow):
    def __init__(self, obj):
        self.user = obj
        super(MainwindowMaps, self).__init__()
        loadUi("../ui/ui/DashboardMaps.ui",self)                 # Here we imported the QT Designer file which we made as Python GUI FIle.
        
        # Command to remove the default Windows Frame Design.
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        
        # Command to make the backgroud of Window transparent.
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        #These 2 lines are used to put funnctions on close and minimize buttons.
        # self.MinimizeButton.clicked.connect(lambda: self.showMinimized())
        
        # ----------------Side bar buttons------------------------------
        self.btnClose.clicked.connect(lambda: self.close())
        self.btnExit.clicked.connect(self.displayLogin)     
        self.btnHome.clicked.connect(self.displayLogin)
        self.btnCustomers.clicked.connect(self.displayLogin)
        self.btnAOrders.clicked.connect(self.displayLogin)
        self.btnDOrders.clicked.connect(self.displayLogin)
        # ----------------Window buttons--------------------------------
        self.btnSearch.clicked.connect(self.SearchGraph)
        self.btnFind.clicked.connect(self.FindCost)
        self.btnInsertNode.clicked.connect(self.InsertNode)
        self.btnGraph.clicked.connect(self.SketchMap)
        self.btnMap.clicked.connect(self.displayMap)
        self.btnAddEdge.clicked.connect(self.InsertEdge)
        self.btnReset.clicked.connect(self.reset)

    def reset(self):
        self.txtComments.setText("Enjoy the best version of the Program!!!")
        self.txtRoute.setText("Route between the nodes")
        self.txtSearch.clear()
        self.txtStartingNode.clear()
        self.txtStartingNode2.clear()
        self.txtEndingNode.clear()
        self.txtEndingNode2.clear()
        self.txtOutput.clear()
        self.txtWeight.clear()
        self.radioBFS.setChecked(False)
        self.radioDFS.setChecked(False)

    def InsertEdge(self):
        s = self.txtStartingNode2.text()
        e = self.txtEndingNode2.text()
        w = self.txtWeight.text()
        if s != "" and e != "" and w != "":
            self.reset()
            graphDisplay.add_edge(s, e, int(w))
            graphCalculate.add_connection(s, e, int(w))
        else:
            self.txtComments.setText("Please enter a valid Edge.")

    def InsertNode(self):
        city = self.txtSearch.text()
        if city != "":
            self.reset()
            graphDisplay.add_vertex(city)
            graphCalculate.add_city(city)
        else:
            self.txtComments.setText("Please enter a valid City Name.")

    def FindCost(self):
        s = self.txtStartingNode.text()
        e = self.txtEndingNode.text()
        if s != "" and e != "":
            cost, route = FindShortestPath(graphCalculate, s, e)
            self.txtOutput.setText(str(cost))
            self.txtRoute.setText(str(route))
        else:
            self.txtComments.setText("Please enter a valid Starting and Ending Node.")

    def SearchGraph(self):
        criteria = None
        query = self.txtSearch.text()
        if self.radioBFS.isChecked() or self.radioDFS.isChecked():
            criteria = self.radioBFS.isChecked()
        
        if query != "" and criteria != None:
            self.txtComments.setText("Enjoy the best version of program!!!")
            self.txtSearch.clear()
            self.radioBFS.setChecked(False)
            self.radioDFS.setChecked(False)
            result = None
            if criteria == True:
                result = graphDisplay.bfs(graphDisplay.find_vertex("UET"), query)
            else:
                result = graphDisplay.dfs(graphDisplay.find_vertex("UET"), query)
            if result:
                self.txtComments.setText("The location Spot is successfully founded in graph!!!")
            else:
                self.txtComments.setText("The location Spot is not Founded in graph!!!")
        else:
            self.txtComments.setText("Please enter a valid Criteria.")

    def displayMap(self):
        self.map_window = WindowImage()
        self.map_window.show()

    def SketchMap(self):
        graphDisplay.visualize()

    def displayLogin(self):
        self.close()
        self.user.loginScreen.show()

class MainwindowOrders(QMainWindow):
    def __init__(self, obj):
        self.user = obj
        self.currentDataFrame = None
        super(MainwindowOrders, self).__init__()
        loadUi("../ui/ui/DashboardOrders.ui",self)                 # Here we imported the QT Designer file which we made as Python GUI FIle.
        
        # Command to remove the default Windows Frame Design.
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        
        # Command to make the backgroud of Window transparent.
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        #These 2 lines are used to put funnctions on close and minimize buttons.
        # self.MinimizeButton.clicked.connect(lambda: self.showMinimized())
        
        # ----------------Side bar buttons------------------------------
        self.btnClose.clicked.connect(lambda: self.close())
        self.btnExit.clicked.connect(self.displayLogin)     
        self.btnHome.clicked.connect(self.displayLogin)
        self.btnCustomers.clicked.connect(self.displayLogin)
        self.btnMap.clicked.connect(self.displayLogin)
        
        self.btnAOrders.clicked.connect(self.displayAOrders)
        self.btnDOrders.clicked.connect(self.displayDOrders)
    
    def addToComboBox(self, obj, data):
        obj.clear()
        for i in data:
            obj.addItem(i)

    def displayAOrders(self):
        self.labelOrders.setText("These Orders are pending to be delivered...")
        self.tableViewLoad(dfOrders)
        self.currentDataFrame = dfOrders

        data = dfOrders.values.tolist()
        capital_Queue.clearQueue()
        for i in data:
            temp = Order(i[0], i[1], -1)
            temp.location = i[2]
            temp.name = i[3]
            temp.quantity = i[4]
            temp.price = i[5]
            temp.total = i[6]
            temp.date = i[7]
            capital_Queue.enqueue(temp)

        header = self.currentDataFrame.columns.tolist()
        self.addToComboBox(self.comboColumns, header)
        self.addToComboBox(self.comboColumns2, header)
        self.comboColumns.setCurrentIndex(0)
        self.comboColumns2.setCurrentIndex(0)

    def displayDOrders(self):
        self.labelOrders.setText("These Orders are dispatched to the customers...")
        self.tableViewLoad(dfPrevious)
        self.currentDataFrame = dfPrevious

        header = self.currentDataFrame.columns.tolist()
        self.addToComboBox(self.comboColumns, header)
        self.addToComboBox(self.comboColumns2, header)
        self.comboColumns.setCurrentIndex(0)
        self.comboColumns2.setCurrentIndex(0)
    
    def tableViewLoad(self, data):
        self.currentDataFrame = data
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

    def displayLogin(self):
        self.close()
        self.user.loginScreen.show()

class WindowImage(QMainWindow):
    def __init__(self):
        super(WindowImage, self).__init__()
        loadUi("../ui/ui/Image.ui",self)       

class windowAddUser(QMainWindow):
    def __init__(self, login_screen):
        self.log = login_screen
        super(windowAddUser, self).__init__()
        loadUi("../ui/ui/AddUser.ui",self)                   # Here we imported the QT Designer file which we made as Python GUI FIle.
        
        # Command to remove the default Windows Frame Design.
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        
        # Command to make the backgroud of Window transparent.
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        #These 2 lines are used to put funnctions on close and minimize buttons.
        # self.MinimizeButton.clicked.connect(lambda: self.showMinimized())
        
        self.btnBack.clicked.connect(self.displayLogin)    
        self.btnAdd.clicked.connect(self.add)      
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

    def findExistingUser(self, name, email, contact):
        for i in range(len(usernames)):
            if usernames[i] == name and emails[i] == email and contacts[i] == contact:
                return True
        return False

    def add(self):
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
                password = Encrypt(password)
                new_row = {'Name': name, 'Father Name': Fname, 'Username': username, 'Password': password, 'CNIC': cnic, 'Email': email, 'Contact No.': contact, 'Location': location}
                df = df._append(new_row, ignore_index=True)
                
                df.to_csv('customerData.csv', index=False)

                self.comments.setText("User is Added Successfully!!!")
            else:
                self.comments.setText("Such User is already present!!!")

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

class windowAddMedicine(QMainWindow):
    def __init__(self, login_screen):
        self.log = login_screen
        super(windowAddMedicine, self).__init__()
        loadUi("../ui/ui/AddMedicine.ui",self)
        
        # Command to remove the default Windows Frame Design.
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        
        # Command to make the backgroud of Window transparent.
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        #These 2 lines are used to put funnctions on close and minimize buttons.
        # self.MinimizeButton.clicked.connect(lambda: self.showMinimized())
        
        self.btnBack.clicked.connect(self.displayLogin)    
        self.btnAdd.clicked.connect(self.add)      
        self.txtName.textChanged.connect(lambda: self.resetStyling(self.txtName))
        self.txtManufacturer.textChanged.connect(lambda: self.resetStyling(self.txtManufacturer))
    
    def resetCombo(self, obj):
        obj.setStyleSheet("background-color: #cdb4db;\nborder: 2px solid #555555;\ncolor:rgba(0,0,0,240);")
    def resetStyling(self, obj):
        obj.setStyleSheet("border: 2px solid #555555;\nbackground-color:rgba(0,0,0,0);\nborder-bottom:2px solid rgba(46,82,101,200);\ncolor:rgba(0,0,0,240);\npadding-bottom:0px;	")

    def displayLogin(self):
        self.close()

    def findExistingUser(self, name, email, contact):
        for i in range(len(usernames)):
            if usernames[i] == name and emails[i] == email and contacts[i] == contact:
                return True
        return False

    def add(self):    
        global dfMedicine 
        name = self.txtName.text()
        price = self.spinPrice.value()
        manufacturer = self.txtManufacturer.text()
        type = self.comboType.currentText()
        discount = self.comboDiscount.currentText()
        size = self.txtSize.text()
        cmp1 = self.txtCmp1.text()
        cmp2 = self.txtCmp2.text()
        
        if name != "" and manufacturer != "":
            self.txtName.clear()
            self.spinPrice.setValue(1)
            self.txtManufacturer.clear()
            self.comboType.setCurrentIndex(0)
            self.comboDiscount.setCurrentIndex(0)
            self.txtSize.clear()
            self.txtCmp1.clear()
            self.txtCmp2.clear()
            new_row = {'Name': name, 'Price': price, 'Discount': discount, 'Manufacturer': manufacturer, 'Type': type, 'Size': size, 'Composition1': cmp1, 'Composition2': cmp2}
            dfMedicine = dfMedicine._append(new_row, ignore_index=True)
            dfMedicine.to_csv('data.csv', index=False)
            self.comments.setText("Medicine is added Successfully!!!")
        else:
            self.comments.setText("Enter the valid Data!!!")

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
