

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
from Algos.GraphDisplay import *
from FormsClasses import *

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
    def __init__(self, userObject):
        self.user = userObject
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
        self.btnCustomers.clicked.connect(self.showCustomers)
        # self.btnCustomers.clicked.connect(partial(self.tableViewLoad, df))
        self.btnAOrders.clicked.connect(partial(self.tableViewLoad, dfOrders))
        self.btnMap.clicked.connect(self.displayMap)
        
        # self.btnLogin.clicked.connect(self.login)

    def showCustomers(self):
        data = df.values.tolist()
        for i in range(len(data)):
            data[i][3] = Decrypt(data[i][3])
        new_df = pd.DataFrame(data, columns=df.columns)
        self.tableViewLoad(new_df)
    
    def displayMap(self):
        self.hide()
        self.maps = MainwindowMaps(self.user)
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
        
        # ----------------Window buttons--------------------------------
        self.btnSearch.clicked.connect(self.SearchGraph)
        self.btnFind.clicked.connect(self.FindCost)
        self.btnInsertNode.clicked.connect(self.InsertNode)
        self.btnGraph.clicked.connect(self.SketchMap)
        self.btnMap.clicked.connect(self.displayMap)

    def InsertNode(self):
        pass

    def FindCost(self):
        pass

    def SearchGraph(self):
        pass

    def displayMap(self):
        self.map_window = WindowImage()
        self.map_window.show()

    def SketchMap(self):
        g = Graph()
        dataSet2(g)
        g.visualize()

    def displayLogin(self):
        self.close()
        self.user.loginScreen.show()

class WindowImage(QMainWindow):
    def __init__(self):
        super(WindowImage, self).__init__()
        loadUi("../ui/ui/Image.ui",self)       