# https://leetcode.com/problems/merge-sorted-array
# 40 ms, faster than 78.33% of Python3 online submissions for Merge Sorted Array.
# seems slow to sort something that already sorted...

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[:] = sorted(nums1[:m] + nums2[:n])