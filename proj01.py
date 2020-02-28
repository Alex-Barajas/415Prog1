# Alex Barajas-Ritchie
# Alondra Lona
# test test test
# CS415 Project01

import matplotlib.pyplot as plt
import numpy as np

count_global = 0

def fib(k):
    global count_global
    # compute the kth fibonacci number
    if k <= 1:
        return k
    else:
        count_global += 1
        return fib(k - 1) + fib(k - 2)


def fibplot(n):
    terms = [0, 1]
    i = 2
    while i <= n:
        terms.append(terms[i-1]+terms[i-2])
        i = i + 1
    return terms


# def fib2(k):
#     # calculate corresponding number of additions
#     if (k == 0) or (k == 1):
#         return 0
#     else:
#         return fib2(k - 1) + fib2(k - 2) + 1


def gcd(m, n):
    global count_global
    if n == 0:
        return m
    count_global += 1
    return gcd(n, m % n)

# def gcdplot(m, n):
#     if n == 0:
#         return 0
#     return gcdplot(n, m % n) + 1

def decreasebyconstant(a, n):
    global count_global
    if n == 0:
        return 1
    if n % 2 == 0:
        count_global += 1
        return (decreasebyconstant(a, n/2))**2
    else:
        count_global += 2
        return (decreasebyconstant(a, (n//2)) ** 2) * a


# def decreasebyconstantplot(a, n):
#     if n == 0:
#         return 0
#     if n % 2 == 0:
#         return decreasebyconstantplot(a, n/2) + 1
#     return decreasebyconstantplot(a, (n // 2)) + 2


def decreasebyone(a, n):
    global count_global
    if n == 0:
        return 1
    if n > 0:
        count_global += 1
        return a * (decreasebyone(a, n - 1))


# def decreasebyoneplot(a, n):
#     if n == 0:
#         return 1
#     return decreasebyoneplot(a, n - n) + n


def divideandconquer(a, n):
    global count_global
    if n == 0:
        return 1
    if n % 2 == 0:
        count_global += 1
        return divideandconquer(a, n/2) * divideandconquer(a, n/2)
    else:
        count_global += 2
        return (divideandconquer(a, (n // 2)) * (divideandconquer(a, (n // 2)))) * a


# def divideandconquerplot(a, n):
#     if n == 0:
#         return 1
#     if n % 2 == 0:
#         return 2 * (divideandconquerplot(a, n // 2)) + 1
#     else:
#         return 2 * (divideandconquerplot(a, n//2)) + 2


def selectionsort(array):
    global count_global
    for i in range(len(array)):
        minidx = i
        for j in range(i+1, len(array)):
            count_global += 1
            if array[minidx] > array[j]:
                minidx = j
        array[i], array[minidx] = array[minidx], array[i]


# def selectionsortplot(array):
#     count = 0
#     for i in range(len(array)):
#         minidx = i
#         for j in range(i+1, len(array)):
#             count += 1
#             if array[minidx] > array[j]:
#                 minidx = j
#         array[i], array[minidx] = array[minidx], array[i]
#
#     return count

def insertionsort(array):
    global count_global
    for i in range(1, len(array)):
        ind = array[i]
        j = i - 1
        while j >= 0 and ind < array[j]:
            count_global += 1
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = ind

# def insertionsortplot(array):
#     count = 0
#     for i in range(1, len(array)):
#         ind = array[i]
#         j = i - 1
#         while j >= 0 and ind < array[j]:
#             count += 1
#             array[j + 1] = array[j]
#             j -= 1
#         array[j + 1] = ind
#     return count

def main():

    global count_global
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
        print("Enter integer value for a and n ( same line ):  \n > ", end='')
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
        print("\nTask 1:")
        print("Fib Seq")
        fibseq = fibplot(66)
        for ele in fibseq:
            print(ele)
        print("_______________________________")
        print("\nTask 2:")
        x, n, w, v, f, g = [], [], [], [], [], []
        for i in range(1, 60):
            n.append(i)

            decreasebyone(5, i)
            x.append(count_global)
            count_global = 0

            decreasebyconstant(5, i)
            w.append(count_global)
            count_global = 0

            divideandconquer(5, i)
            v.append(count_global)
            count_global = 0


            gcd(fibseq[i+2], fibseq[i-1])
            g.append(count_global)
            count_global = 0

        #plt.scatter(x, y, color='k')
        plt.scatter(n, g, c='c', marker='o', label='fib -> GCD')
        # plt.legend(loc='upper right')
        plt.title("Task 1 Graph: Fib -> GCD")
        plt.show()

        plt.xlim(0, 60)
        plt.ylim(0, 60)
        plt.scatter(n, x, c='b', marker='x', label='Decrease by One')
        plt.scatter(n, w, c='r', marker='s', label='Decrease by Constant')
        plt.scatter(n, v, c='g', marker='o', label='Divide and Conquer')
        # plt.scatter(n, f, c='c', marker='o', label='Divide and Conquer')
        # plt.scatter(n, g, c='c', marker='o', label='fib -> GCD')
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
         #   x.append(insertionsortplot(5,))
          #  n.append(i)

        randomarray = np.random.randint(1, 101, 60)
        randomarray.sort()
        print(insertionsort(randomarray))

        plt.xlim(0, 45)
        plt.ylim(0, 45)
        plt.scatter(n, x, c='b', marker='x', label='Insertion Sort')
        plt.scatter(n, w, c='r', marker='s', label='Selection Sort ')
        plt.legend(loc='upper right')
        plt.title("Task 3 Graph: Best Case")
        plt.show()

main()
