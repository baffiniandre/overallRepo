import matplotlib.pyplot as plt
import numpy as np

def printer():
    string = input("Type string: ")
    return print(string)

def linkedList(sizeList):
    list = []
    i = 0
    #sizeList = int(input('Enter list size: '))
    while i < sizeList:
        list.append(input('Enter ' + str(i+1)  + ' list value: '))
        i += 1
    return list

def matrix():
    print('Matrix creation:\n')
    matrix = []
    m = int(input('Enter rows: \n'))
    n = int(input('Enter column: \n'))
    i = 0
    j = 0
    while i < m:
        while j < n:
            row = linkedList(n)
            matrix.append(row)
            j += 1
        i += 1
    return matrix

def simplePlot():
    fig, ax = plt.subplots()             # Create a figure containing a single Axes.
    ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the Axes.
    plt.show()                           # Show the figure.


#def printer():
#    return print(input("String: "))

def main():
    #print(linkedList())
    #print(matrix())
    simplePlot()

if __name__ == "__main__":
    main()