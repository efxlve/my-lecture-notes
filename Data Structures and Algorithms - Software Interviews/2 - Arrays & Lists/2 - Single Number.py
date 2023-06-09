#Single Number
#Given a non-empty array of integers, every element appears twice except for one. Find that single one.
#Note:
#Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

#Example 1:
#Input: [2,2,1]
#Output: 1

#Example 2:
#Input: [4,1,2,1,2]
#Output: 4

#Example 3:
#Input: [1]
#Output: 1

myList = [4,1,2,1,2]

#Solution
def solution2():
    result = 0 #xor with zero. zero does not change xor result.
    for num in myList:
        result ^= num #Xor with number
    return result

print(solution2()) #4 #Bit Manipulation