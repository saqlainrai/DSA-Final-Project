
import pandas as pd
from BubleSort import bubble_sort
from InsertionSort import insertion_sort
from RedBlack import RBT
from stack_implementation import Stack
from linearSearch import linearSearch

def checkRBT():
    tree = RBT()
    tree.insert(1)
    tree.insert(2)
    tree.insert(3)
    tree.insert(4)
    tree.insert(5)
    tree.insert(6)
    tree.insert(7)
    print(tree.Root)
def checkStack():
    stack = Stack()
    stack.push(5)
    stack.push(5)
    stack.push(10)
    stack.push("sami")

    print("after push operation", stack.stack)  #display function

    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()

    print("after pop operation", stack.stack)
def checkSearch():
    array = [['1', '2', '3', '4'],
            ['4', '2', '1', '8'],
            ['3', '2', '6', '7'],
            ['4', '7', '4', '1'],
            ['4', '2', '1', '3']]
    
    # for i in array:
    #     print(i)
    df = linearSearch(array, '2', 1)
    for i in df:
        print(i)

def main():
    # checkRBT()
    # checkStack()
    checkSearch()

if __name__ == "__main__":
    main()