
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QFileDialog
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5 import QtCore, QtWidgets
from PyQt5.uic import loadUi
from functools import partial
import pandas as pd

from algorithms import *
from Capital_Algos import *

def validate(name, password):
    if name == "admin" and password == "1234":
        return True
    else:
        return False

class Mainwindow(QMainWindow):
    def __init__(self):
        super(Mainwindow, self).__init__()
        loadUi("untitled.ui",self)                 # Here we imported the QT Designer file which we made as Python GUI FIle.
        
        # Command to remove the default Windows Frame Design.
        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        
        # Command to make the backgroud of Window transparent.
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        #These 2 lines are used to put funnctions on close and minimize buttons.
        # self.MinimizeButton.clicked.connect(lambda: self.showMinimized())
        # self.CrossButton.clicked.connect(lambda: self.close())                        add cross(close) button
        
        # self.loadBtn.clicked.connect(self.tableViewLoad(self, data))

def main():
        import sys
        app = QtWidgets.QApplication(sys.argv)
        # MainWindow = QtWidgets.QMainWindow()
        window = Mainwindow()
        window.show()
        sys.exit(app.exec_())

if __name__ == "__main__":
        main()
