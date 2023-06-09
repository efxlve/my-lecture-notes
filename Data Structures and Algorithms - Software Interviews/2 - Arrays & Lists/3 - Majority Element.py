#Majority Element
#Given an array of size n, find the majority element. The majority element is the element that appears more than floor(n/2) times.
#You may assume that the array is non-empty and the majority element always exist in the array.

#Example 1:
#Input: [3,2,3]
#Output: 3

#Example 2:
#Input: [2,2,1,1,1,2,2]
#Output: 2

myList = [2,2,1,1,1,2,2]

#Solution 0
#Solution below is O(n) for time and space. 
def solution():
    count = {}
    result = 0
    maxCount = 0
    for num in myList:
        count[num] = 1 + count.get(num,0)
        if count[num] > maxCount:
            result = num
        maxCount = max(maxCount,count[num])
    return result

print(solution()) #2

#Solution 1 - Boyer-Moore Voting Algorithm
#Boyer-Moore algorithm for O(1) space and O(n) time
def solution2():
    result = 0
    count = 0
    for num in myList:
        if count == 0:
            result = num
        if num == result:
            count += 1
        else:
            count -= 1
    return result

print(solution2()) #2

#or

def solution3():
    result = 0
    count = 0
    for num in myList:
        if count == 0:
            result = num
        count += 1 if num == result else -1
    return result

print(solution3()) #2