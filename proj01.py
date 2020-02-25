# Alex Barajas-Ritchie
# Alondra Lona
# test test test
# CS415 Project01

import matplotlib.pyplot as plt
import numpy as np


def fib(k):
    # compute the kth fibonacci number
    if k <= 1:
        return k
    else:
        return fib(k - 1) + fib(k - 2)


def fib2(k):
    # calculate corresponding number of additions
    if (k == 0) or (k == 1):
        f = 0
    else:
        f = fib2(k - 1) + fib2(k - 2) + 1
    return f


def gcd(m, n):
    if m == 0:
        return n
    return gcd(n % m, m)


def decreasebyconstant(a, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return decreasebyconstant(a, n/2) * decreasebyconstant(a, n/2)
    else:
        return (decreasebyconstant(a, ((n-1)/2)) * decreasebyconstant(a, (n-1)/2)) * a


def decreasebyconstantplot(a, n):
    return 1


def decreasebyone(a, n):
    if n == 0:
        return 1
    return decreasebyone(a, n - 1) * a


def decreasebyoneplot(a, n):
    if n == 0:
        return 1
    return decreasebyone(a, n - 1) + 1


def divideandconquer(a, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return divideandconquer(a, n/2) * divideandconquer(a, n/2)
    else:
        return (divideandconquer(a, (n-1)/2) * divideandconquer(a, (n-1)/2)) * a

def divideandconquerplot(a, n):
    return 2

def selectionsort(array):
    for i in range(len(array)):
        minidx = i
        for j in range(i+1, len(array)):
            if array[minidx] > array[j]:
                minidx = j
        array[i], array[minidx] = array[minidx], array[i]


def insertionsort(array):
    for i in range(1, len(array)):
        ind = array[i]
        j = i - 1
        while j >= 0 and ind < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = ind


def main():
    print("_______________________________")
    mode = int(input("Mode selection: \n \t Enter 0 for User Testing Mode --or--  1 Scatter Plot Mode: \n > "))
    if mode == 0:
        print("_______________________________")
        print("User Testing Mode selected!")
        print("_______________________________")
        #print("Enter integer value for K:  \n > ", end='')
        #array = list(map(int, input().split()))
        print("\nTask 1:")
        k = int(input("\tEnter integer value for K:  \n > "))
        print("Fib: ", fib(k))
        print("GCD: ", gcd(k+1, k))
        print("_______________________________")
        print("\nTask 2:")
        print("Enter integer value for a and n:  \n > ", end='')
        array = list(map(int, input().split()))
        if len(array) <= 1:
            exit()
        a, n = array[0], array[1]
        print("Decrease by One method:", decreasebyone(a, n))
        print("Decrease by a Constant Method: ", decreasebyconstant(a, n))
        print("Divide and conquer method: ", divideandconquer(a, n))

        print("_______________________________")
        print("\nTask 3:")
        n = int(input("Enter a size of a list:  \n > "))
        #print("Enter a list of integers to be sorted:  \n > ", end='')
        #array = list(map(int, input().split()))
        sortarray = []
        print("Enter elements in list on its own line")
        for ele in range(n):
            sortarray.append(input())
        selectarray = list.copy(sortarray)
        insertionarray = list.copy(sortarray)
        selectionsort(selectarray)
        insertionsort(insertionarray)
        print("Orginal")
        for ele in sortarray:
            print(ele, end=' ')
        print("\nSelection Sort")
        for ele in selectarray:
            print(ele, end=' ')
        print("\nInsertion Sort")
        for ele in insertionarray:
            print(ele, end=' ')

    if mode == 1:
        print("Scatter plot mode selected")
        for i in range(1, 11):
            print(gcd(fib(i + 1), fib(i)))

        print("_______________________________")
        print("\nTask 2:")
        print("Decrease by One")
        x, y, w, v = [], [], [], []
        for i in range(1, 5):
            x.append(decreasebyoneplot(2, i))
            w.append(decreasebyconstantplot(2, i))
            v.append(divideandconquerplot(2, i))
            y.append(i)
        #plt.scatter(x, y, color='k')
        plt.scatter(x, y, c='b', marker='x', label='Decrease by One')
        plt.scatter(w, y, c='r', marker='s', label='Decrease by Constant')
        plt.scatter(v, y, c='g', marker='s', label='Divide and Conquer')
        plt.legend(loc='upper left')
        plt.title("Task 2 Graph")
        plt.show()






main()
