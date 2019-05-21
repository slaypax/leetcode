# https://leetcode.com/problems/maximum-product-of-three-numbers/submissions/
# https://leetcode.com/submissions/detail/230327797/

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        # two smallest and largest (because negatives) or three largest
        return max([nums[0] * nums[1] * nums[-1], nums[-3] * nums[-2] * nums[-1]])