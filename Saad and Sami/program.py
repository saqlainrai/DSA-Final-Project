
import pandas as pd
from BubleSort import bubble_sort
from InsertionSort import insertion_sort

def main():
    # df = pd.read_csv("medicineData.csv")
    array = [[9, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
    insertion_sort(array, 0, True)
    # pd.to_csv("medicine.csv")
    print(array)
    print("SUCCESS")

if __name__ == "__main__":
    main()