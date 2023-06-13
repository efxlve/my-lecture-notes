#Recursion
def calculateFactorial(n):
    # edge case - exit condition
    if n == 1:
        return 1
    else:
        return n * calculateFactorial(n-1)
    
print(calculateFactorial(5)) # 120

def calculateContinuousSum(n):
    # edge case - exit condition
    if n == 0:
        return 0
    else:
        return n + calculateContinuousSum(n-1)
    
print(calculateContinuousSum(5)) # 15

