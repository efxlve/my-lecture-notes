#Reserve String
#Write a function that reverses a string. The input string is given as an array of characters s.
#You must do this by modifying the input array in-place with O(1) extra memory.

#Example 1:
#Input: s = ["h","e","l","l","o"]
#Output: ["o","l","l","e","h"]

#Example 2:
#Input: s = ["H","a","n","n","a","h"]
#Output: ["h","a","n","n","a","H"]

#Constraints:
#1 <= s.length <= 105
#s[i] is a printable ascii character.

myArray = ["h","e","l","l","o"]

#Solution 1 - Using Recursion
#Time complexity: O(n)
#Space complexity: O(n)
def reverseRecursive(s, start:int, end:int):
    if start >= end:
        return
    else:
        s[start], s[end] = s[end], s[start]
        reverseRecursive(s, start+1, end-1)

reverseRecursive(myArray, 0, len(myArray)-1)
print(myArray) # ['o', 'l', 'l', 'e', 'h']

#Solution 2 - Using Iteration
#Time complexity: O(n)
#Space complexity: O(1)
def reverseIterative(s):
    start = 0
    end = len(s)-1
    while start < end:
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1

reverseIterative(myArray)
print(myArray) # ['h', 'e', 'l', 'l', 'o']





