import sys
import csv
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("CSV Data Viewer")
        self.setGeometry(100, 100, 600, 400)




        self.centralWidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.centralWidget)
        self.layout = QtWidgets.QHBoxLayout(self.centralWidget)

        self.widgetContainer = QtWidgets.QWidget(self.centralWidget)
        self.layout.addWidget(self.widgetContainer)
        self.rightLayout = QtWidgets.QVBoxLayout(self.widgetContainer)






        self.tableWidget = QtWidgets.QTableWidget()
        self.tableWidget.setRowCount(8)  # Set row count
        self.tableWidget.setColumnCount(8)  # Set column count
        self.tableWidget.setHorizontalHeaderLabels(
            ["Column 0", "Column 1", "Column 2", "Column 3", "Column 4", "Column 5", "Column 6", "Column 7"])
        self.rightLayout.addWidget(self.tableWidget)

        # Load data from CSV
        self.load_data_from_csv()



        # Set size policy to minimize the table
        self.tableWidget.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)


    def get_data_from_table(self):
        rows = self.tableWidget.rowCount()
        cols = self.tableWidget.columnCount()
        data = []

        for row in range(rows):
            row_data = []
            for col in range(cols):
                item = self.tableWidget.item(row, col)
                row_data.append(item.text())
            data.append(row_data)

        return data

    def load_data_from_csv(self):
        file_path = r'A:\scrapping data\medicineData.csv'
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = list(csv.reader(file))

            # Set row and column count based on your data size
            self.tableWidget.setRowCount(8)  # Set row count
            self.tableWidget.setColumnCount(8)  # Set column count
            for row_index, row_data in enumerate(data[:8]):  # Limit data to 8 rows
                for col_index, cell_data in enumerate(row_data[:8]):  # Limit to 8 columns
                    item = QtWidgets.QTableWidgetItem(cell_data)
                    self.tableWidget.setItem(row_index, col_index, item)
        except FileNotFoundError:
            print(f"File not found: {file_path}")

    def update_table(self, data, column_index):
        for row, row_data in enumerate(data):
            for col, cell_data in enumerate(row_data):
                item = QtWidgets.QTableWidgetItem(cell_data)
                self.tableWidget.setItem(row, col, item)





def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
