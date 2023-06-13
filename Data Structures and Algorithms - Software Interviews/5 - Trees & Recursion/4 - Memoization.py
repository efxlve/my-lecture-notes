#Memoization
#Memoization is a technique for improving the performance of recursive algorithms. It involves rewriting the recursive algorithm so that as answers to problems are found, they are stored in an array. The next time the same problem is encountered, the value in the array is returned, saving the computation time at the expense of a (usually) modest amount of space.

myList = [5, 10, 15, 5, 20, 15, 5, 10, 5, 100, 10, 20, 15, 100, 5, 10]

#Solution - Using Memoization
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

memo = {}

def memoizationSolution(n):
    if n in memo:
        return memo[n]
    else:
        memo[n] = calculateFibonacciIterative(n)
        return memo[n]

print(memoizationSolution(8)) # 21


