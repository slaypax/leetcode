#  https://leetcode.com/problems/find-the-duplicate-number/


# Runtime: 44 ms, faster than 61.61% of Python3 online submissions for Find the Duplicate Number.
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        nums_map = collections.Counter(nums)
        
        for i, n in enumerate(nums_map):
            if nums_map[n] != 1:
                return n