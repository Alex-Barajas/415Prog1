# Alex Barajas-Ritchie 
# Alondra Lona
# CS415 Project01

import math

def main ():

    #print(fib(3))

    main()



def fib (k):

      if (k <= 1):
         return k
      else:
         return fib(k-1) + fib(k-2)

#print (fib(int(input())))

def fib2(k):
    if (k == 0 or k == 1):
        f=0
    else:
        f = fib2(k-1) + fib2(k-2) + 1
    return f
print(fib2(int(input())))