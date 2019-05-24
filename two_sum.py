# https://leetcode.com/problems/two-sum/
# Given an array of integers, return indices of the two numbers such that they
# add up to a specific target.
# You may assume that each input would have exactly one solution, 
# and you may not use the same element twice.

# Your runtime beats 85.58 % of python3 submissions.
# Runtime: 40 ms

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}                
        for i in range(len(nums)):
            n = nums[i]
            if n in nums_dict:
                return nums_dict[n], i
            else:
                nums_dict[target -n] =i