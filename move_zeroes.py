# https://leetcode.com/problems/move-zeroes/
#
# Runtime: 48 ms, faster than 82.91% of Python3 online submissions for Move Zeroes.

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroes = 0
        ans = []
        for n in nums:
            if n == 0:
                zeroes += 1
            else:
                ans.append(n)
                
        for i in range(zeroes):
            ans.append(0)
            
        for i in range(len(nums)):
            nums[i] = ans[i]