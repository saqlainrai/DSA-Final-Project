
def BubbleSort(array,rowNumber):
    for i in range(0,len(array[rowNumber])):
        for j in range(len(array[rowNumber])-1,0,-1):
            if(array[rowNumber][j] < array[rowNumber][j - 1]):
                for i in range(0,7):
                    array = exchangeColumns_b(array, j, j-1)
    return array

def InsertionSort(array_2, rowNumber):
    for i in range(1, len(array_2[rowNumber])):
        key = getColumnFrom2D(array_2, i)
        j = i - 1
        while(j >= 0 and key[rowNumber] <= array_2[rowNumber][j]):
            array_2 = exchangeColumns(array_2, j+1, j)
            j = j - 1
        exchangeObject(array_2, j+1, key)

    return array_2

def exchangeObject(array, columnNo, key):
    for i in range(len(key)):
        array[i][columnNo] = key[i]

def SelectionSort(array , rowNumber):
    for i in range (0,len(array[rowNumber])):
        minIndex = minimum(array, i,rowNumber)
        array = exchangeColumns_b(array, minIndex, i)
    return array

def MergeSort(arr, rowNumber):
    searchRef = arr[rowNumber].copy()
    searchRef = combineIndex(searchRef)
    MergeSortArr(searchRef, rowNumber, 0, len(searchRef)-1)
    indexList = [x[0] for x in searchRef]
    arr = reCreateNewSortedArr(arr, indexList)
    return arr

def byQuickSort(mainList,rowNumber):
    QuickSort(mainList[rowNumber], rowNumber, 0, len(mainList[0])-1,mainList)
    return mainList

def QuickSort(array, rowNumber, left, right, mainList):
    if(left < right):
        pivot = Sort_asc(array,left,right,mainList)
        QuickSort(array, rowNumber,left, pivot-1,mainList)
        QuickSort(array, rowNumber,pivot+1, right,mainList)




# ------------------------------------Common Functions---------------------------------------

import math
import sys

def Sort_asc(subArray,left,right,mainList):
    pivot = subArray[right]
    i = left - 1
    for k in range(left,right):
        if(subArray[k] <= pivot):
            i = i + 1
            exchangeColumns_Q(k, i, mainList)
    exchangeColumns_Q(right, i+1, mainList)
    return i+1

def Merge(array, p, q, r, rowNumber):
    leftArray = array[p:q+1]
    rightArray = array[q+1:r+1]
    if (isinstance(array[0][rowNumber], int) or isinstance(array[0][rowNumber], float)):
        leftArray.append([len(leftArray), sys.maxsize])
        rightArray.append([len(rightArray), sys.maxsize])
    else:
        maxlen=len(list(max([x[1] for x in leftArray])))+1
        leftArray.append([len(leftArray), ''.join([chr(255)]*maxlen)])
        rightArray.append([len(rightArray), ''.join([chr(255)]*maxlen)])

    leftArrayPointer = 0
    rightArrayPointer = 0

    i = p
    while (i <= r):
        if (leftArrayPointer<len(leftArray) and (leftArray[leftArrayPointer][rowNumber] <= rightArray[rightArrayPointer][rowNumber])):
            array[i] = leftArray[leftArrayPointer]
            leftArrayPointer += 1
        else:
            array[i] = rightArray[rightArrayPointer]
            rightArrayPointer += 1
        i += 1

def reCreateNewSortedArr(unSortedArr, sortedIndexFormat):
    sortedArr = [0]*len(unSortedArr)
    sortedArr = [[] for i in range(len(sortedArr))]
    for i in range(len(sortedIndexFormat)):
        for j in range(len(unSortedArr)):
            sortedArr[j].append(unSortedArr[j][sortedIndexFormat[i]])
    return sortedArr


def MergeSortArr(array, rowNumber, start, end):
    if (start < end):
        q = math.floor((start+end)/2)
        arr = MergeSortArr(array, 1, start, q)
        arr = MergeSortArr(array, 1, q+1, end)
        Merge(array, start, q, end, 1)

def combineIndex(arr):
    arr = [[i, arr[i]] for i in range(len(arr))]
    return arr

def minimum(array , start, rowNumber):
    minimumNumber = array[rowNumber][start]
    minimumIndex = start
    for i in range(start , len(array[rowNumber])):
        if(minimumNumber > array[rowNumber][i]):
            minimumNumber = array[rowNumber][i]
            minimumIndex = i
    return minimumIndex    

def getColumnFrom2D(arr_2, columnNo):
    arr = []
    for i in range(len(arr_2)):
        arr.append(arr_2[i][columnNo])
    return arr

def exchangeColumns_Q(a, b, mainList):
    for i in range(0,7):
        c = mainList[i][a]
        mainList[i][a] = mainList[i][b]
        mainList[i][b] = c

def exchangeColumns_b(array, a, b):
    for i in range(0,7):
        c = array[i][a]
        array[i][a] = array[i][b]
        array[i][b] = c
    return array

def exchangeColumns(array, a, b):
    for i in range(len(array)):
        array[i][a] = array[i][b]
    return array