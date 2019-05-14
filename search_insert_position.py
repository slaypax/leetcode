# https://leetcode.com/problems/search-insert-position/submissions/
# https://leetcode.com/submissions/detail/228558969/

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target == 0:
            return 0
        if target > nums[-1]:
            return len(nums)
        if target < nums[0]:
            return 0
        if target in nums:
            return nums.index(target)

        
        for i, n in enumerate(nums):
            try:
                if n < target and nums[i + 1] > target:
                    return i + 1
            except IndexError:
                return len(nums)