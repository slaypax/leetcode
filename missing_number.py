# https://leetcode.com/problems/missing-number/submissions/
# Memory Usage: 14.6 MB, less than 6.19% of Python3 online submissions for Missing Number.

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # query for 'in' in O(1) time by turning list into set
        number_set = set(nums)
        for number in range(len(nums) + 1):
            if number not in number_set:
                return number

# Guass' formula lol
# Memory Usage: 14 MB, less than 73.85% of Python3 online submissions for Missing Number.

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expected = len(nums) * (len(nums)+ 1) // 2
        actual = sum(nums)
        print(expected)
        return int(expected) - actual