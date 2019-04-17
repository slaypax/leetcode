# https://leetcode.com/problems/intersection-of-two-arrays-ii/
# Given two arrays, write a function to compute their intersection.
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]

# Your runtime beats 32.81 % of python3 submissions
# Runtime: 56 ms

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        x, y = map(collections.Counter, (nums1, nums2))
        return list((x & y).elements())