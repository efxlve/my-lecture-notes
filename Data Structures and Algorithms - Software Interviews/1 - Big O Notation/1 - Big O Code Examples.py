def bigo(n):
    for i in range(n):
        print(i)

bigo(10) # O(n) --> Linear Time

def bigo1(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

bigo1(10) # O(n^2) --> Quadratic Time

def bigo2(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(i, j, k)

bigo2(10) # O(n^3) --> Cubic Time

import math
def logn(n):
    while n > 1:
        n = math.floor(n / 2)
        print(n)

logn(10) # O(log n) --> Logarithmic Time

def nlogn(n):
    lim = n
    while n > 1:
        n = math.floor(n / 2)
        for i in range(1, lim):
            print(i)

nlogn(10) # O(n log n) --> Linearithmic Time

def nfactorial(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n * nfactorial(n - 1) # Recursion
    
print(nfactorial(10)) # O(n!) --> Factorial Time

def twotonfibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return twotonfibonacci(n-1) + twotonfibonacci(n-2) # Recursion

print(twotonfibonacci(10)) # O(2^n) --> Exponential Time

