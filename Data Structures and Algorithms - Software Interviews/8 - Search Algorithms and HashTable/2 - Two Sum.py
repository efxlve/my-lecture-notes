#Two Sum

#Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order.

#Example:
#Given nums = [2, 7, 11, 15], target = 9,
#Because nums[0] + nums[1] = 2 + 7 = 9,
#return [0, 1].

#Example2:
#Given nums = [3, 2, 4], target = 6,
#Because nums[1] + nums[2] = 2 + 4 = 6,
#return [1, 2].

#Solution
class Solution:
    def twoSum(self, nums, target):
        myHashMap = {}
        
        for i, num in enumerate(nums):
            difference = target - num
            if difference in myHashMap:
                return [myHashMap[difference],i]
            myHashMap[num] = i

solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9)) #[0, 1]
print(solution.twoSum([3, 2, 4], 6)) #[1, 2]


