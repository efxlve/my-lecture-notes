#Contains Duplicate
#Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

#Example 1:
#Input: [1,2,3,1]
#Output: true

#Example 2:
#Input: [1,2,3,4]
#Output: false

#Example 3:
#Input: [1,1,1,3,3,4,3,2,4,2]
#Output: true

myList = [1,2,3,1]

#Solution 0
def solution():
    mySet = set()
    for i in myList:
        if i in mySet:
            return True
        else:
            mySet.add(i)
    return False

print(solution()) #True

#Solution 1
def solution2():
    return len(myList) != len(set(myList))

print(solution2()) #True 




