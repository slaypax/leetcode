# https://leetcode.com/problems/intersection-of-two-arrays/submissions/
# Runtime: 28 ms, faster than 99.98% of Python3 online submissions for Intersection of Two Arrays.

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = set(nums1).intersection(set(nums2))
        return list(intersection)