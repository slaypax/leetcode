
# https://leetcode.com/problems/rotate-array/
# Runtime: 52 ms, faster than 81.78% of Python3 online submissions for Rotate Array.

# this is stupid and makes a new list and then just turns the original intothe copy
# I don't think this is a realistic solution at all

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp_list = (nums[(len(nums) - k): len(nums)]) + (nums[0: (len(nums) - k)])
        
        for i, x in enumerate(temp_list):
            nums[i] = x


