# Alex Barajas-Ritchie
# Alondra Lona
# CS415 Project01

import math

def main ():

    #print(fib(3))

    main()


#task 1

def fib (k):
    # compute the kth fibonacci number
      if (k <= 1):
         return k
      else:
         return fib(k-1) + fib(k-2)

print (fib(int(input("Compute the kth fib number: "))))

def fib2(k):
    # calculate corresponding number of additions
    if (k == 0 or k == 1):
        f=0
    else:
        f = fib2(k-1) + fib2(k-2) + 1
    return f
print(fib2(int(input("Compute the number of additions A(k): "))))



# task 2
