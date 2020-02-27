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
        return (decreasebyconstant(a, n/2))**2
    else:
        return (decreasebyconstant(a, (n//2)) ** 2) * a


def decreasebyconstantplot(a, n):
    if n == 0:
        return 0
    if n % 2 == 0:
        return decreasebyconstantplot(a, n/2) + 1
    return decreasebyconstantplot(a, (n // 2)) + 2


def decreasebyone(a, n):
    if n == 0:
        return 1
    if n > 0:
        return a * (decreasebyone(a, n - 1))


def decreasebyoneplot(a, n):
    if n == 0:
        return 1
    return decreasebyoneplot(a, n - n) + n


def divideandconquer(a, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return divideandconquer(a, n/2) * divideandconquer(a, n/2)
    else:
        return (divideandconquer(a, (n // 2)) * (divideandconquer(a, (n // 2)))) * a


def divideandconquerplot(a, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        #return divideandconquerplot(a, n / 2) + divideandconquerplot(a, n / 2) + 1
        return 2 * (divideandconquerplot(a, n // 2)) + 1
    else:
        return 2 * (divideandconquerplot(a, n//2)) + 2
    #return (divideandconquerplot(a, n // 2)) + divideandconquerplot(a, n) + 1

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

def insertionsortplot(array):
    count = 0
    for i in range(1, len(array)):
        ind = array[i]
        j = i - 1
        while j >= 0 and ind < array[j]:
            count += 1
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = ind
    return count

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
        print("Original")
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
        # for i in range(1, 5):
        #     print(gcd(fib(i + 1), fib(i)))

        print("_______________________________")
        print("\nTask 2:")
        x, n, w, v = [], [], [], []
        for i in range(1, 100):
            x.append(decreasebyoneplot(5, i))
            w.append(decreasebyconstantplot(5, i))
            v.append(divideandconquerplot(5, i))
            n.append(i)
        #plt.scatter(x, y, color='k')
        plt.xlim(0, 45)
        plt.ylim(0, 45)
        plt.scatter(n, x, c='b', marker='x', label='Decrease by One')
        plt.scatter(n, w, c='r', marker='s', label='Decrease by Constant')
        plt.scatter(n, v, c='g', marker='o', label='Divide and Conquer')
        plt.legend(loc='upper right')
        plt.title("Task 2 Graph: Worst Case Exponentiation")
        plt.show()



        print ("\nTask 3:")
        #Task 3: For different sizes of the list (n), generate test data that is sorted,
        # random and reverse sorted. Use the same input data to
        # compute C(n) for each of the two sorting algorithms.
        # Produce three scatter plots that compare the complexity
        # of the two algorithms in
        # i) Best-case,
        # ii) Average-case, and
        # iii) Worst-case.
        x, n, w, v = [], [], [], []
        #for i in range (1, 100):
            #x.append(insertionsortplot(5))
           # n.append(i)
        
        plt.xlim(0, 45)
        plt.ylim(0, 45)
        plt.scatter(n, x, c='b', marker='x', label='Insertion Sort')
        plt.scatter(n, w, c='r', marker='s', label='Selection Sort ')
        plt.legend(loc='upper right')
        plt.title("Task 3 Graph: Best Case")
        plt.show()






main()
