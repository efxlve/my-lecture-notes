#Find The Duplicate Number
#https://leetcode.com/problems/find-the-duplicate-number/
# ==============================================================================
# Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive),
# prove that at least one duplicate number must exist.
# Assume that there is only one duplicate number, find the duplicate one.
# ==============================================================================
# Example:
# Input: [1,3,4,2,2]
# Output: 2
# ==============================================================================
# Algorithm:
# 1. Use Floyd's Tortoise and Hare (Cycle Detection) algorithm
# 2. Find the intersection point of the two runners
# 3. Move slow pointer to the beginning of the list
# 4. Move both pointers at the same speed until they meet at the beginning of the cycle
# ==============================================================================
# Time Complexity: O(n)
# Space Complexity: O(1)
# ==============================================================================
# Solution Explanation:
# https://leetcode.com/problems/find-the-duplicate-number/solution/
# ==============================================================================
def floydSolution():
    nums = [1,3,4,2,2]
    slow = nums[0]
    fast = nums[0]

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow

print(floydSolution())  # 2
