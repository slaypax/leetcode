# Runtime: 39 ms
# Runtime: 40 ms, faster than 93.24% of Python3 online submissions for Single Number.
class Solution(object):
    def singleNumber(self, nums):

        x = 0
        for i in nums: 
            x ^= i
        return x