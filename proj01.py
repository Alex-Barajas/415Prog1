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

print (fib(int(input())))

