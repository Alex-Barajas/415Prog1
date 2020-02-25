# Alex Barajas-Ritchie
# Alondra Lona
# test test test
# CS415 Project01

import math



def fib(k):

    # compute the kth fibonacci number
    if (k <= 1):
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

    if (m == 0):
        return n
    return gcd(n % m, m)




def main():
    #print(fib(int(input("Compute the kth fib number: "))))
    #print(fib2(int(input("Compute the number of additions A(k): "))))
    for i in range(1,11):
        print(gcd(fib(i+1),fib(i))) 


main()