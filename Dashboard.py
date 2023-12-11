
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QFileDialog
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5 import QtCore, QtWidgets
from PyQt5.uic import loadUi
from functools import partial
import pandas as pd
import csv

from algorithms import *
from Capital_Algos import *

dfMedicine = pd.read_csv('medicineData.csv')
dfCustomers = pd.read_csv('customerData.csv')
dfOrders = pd.read_csv('ordersData.csv')

def validate(name, password):
    if name == "admin" and password == "1234":
        return True
    else:
        return False

class MainwindowDashboard(QMainWindow):
    def __init__(self, login_screen):
        self.log = login_screen
        super(MainwindowDashboard, self).__init__()
        loadUi("ui/ui/21.ui",self)                 # Here we imported the QT Designer file which we made as Python GUI FIle.
        
        # Command to remove the default Windows Frame Design.
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        
        # Command to make the backgroud of Window transparent.
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        #These 2 lines are used to put funnctions on close and minimize buttons.
        # self.MinimizeButton.clicked.connect(lambda: self.showMinimized())
        
        self.btnClose.clicked.connect(lambda: self.close())                       #add cross(close) button
        self.btnExit.clicked.connect(self.displayLogin)                       #add cross(close) button
        self.btnHome.clicked.connect(partial(self.tableViewLoad, dfMedicine))
        self.btnCustomers.clicked.connect(partial(self.tableViewLoad, dfCustomers))
        self.btnAOrders.clicked.connect(partial(self.tableViewLoad, dfOrders))
        
        # self.btnLogin.clicked.connect(self.login)

    def displayLogin(self):
        self.close()
        self.log.show()

    def loadData(self, filename):
        try:
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                self.model.clear()

                # Set horizontal header labels
                header = next(reader)
                self.model.setHorizontalHeaderLabels(header)

                # Populate the model with data
                for row_data in reader:
                    row = [QStandardItem(cell) for cell in row_data]
                    self.model.appendRow(row)

                # Set the model for the table view
                self.tableView.setModel(self.model)
        except FileNotFoundError:
            print(f"File not found: {filename}")

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

    def login(self):
        self.close()
        self.window = QtWidgets.QMainWindow()
        # self.ui = Ui_MainWindow()
        loadUi("untitled1.ui",self.ui)

def main():
        import sys
        app = QtWidgets.QApplication(sys.argv)
        # MainWindow = QtWidgets.QMainWindow()
        window = MainwindowDashboard()
        window.show()
        sys.exit(app.exec_())

if __name__ == "__main__":
        main()
