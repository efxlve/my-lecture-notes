#Fibonacci
#The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones,
#starting from 0 and 1. That is,

#F(0) = 0, F(1) = 1
#F(n) = F(n - 1) + F(n - 2), for n > 1.

#Given n, calculate F(n).

#Example 1:
#Input: n = 2
#Output: 1
#Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

#Example 2:
#Input: n = 3
#Output: 2
#Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

#Example 3:
#Input: n = 4
#Output: 3
#Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.

#Constraints:
#0 <= n <= 30

#Solution 1 - Using Recursion
#Time complexity: O(2^n)
#Space complexity: O(n)
def calculateFibonacciRecursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return calculateFibonacciRecursive(n-1) + calculateFibonacciRecursive(n-2)
    
print(calculateFibonacciRecursive(8)) # 21

#Solution 2 - Using Iteration
#Time complexity: O(n)
#Space complexity: O(1)
def calculateFibonacciIterative(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        first = 0
        second = 1
        for i in range(2, n+1):
            third = first + second
            first = second
            second = third
        return third
    
print(calculateFibonacciIterative(8)) # 21