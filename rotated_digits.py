# https://leetcode.com/problems/rotated-digits/
# Runtime: 124 ms, faster than 39.27% of Python3 online submissions for Rotated Digits.

class Solution:
    def rotatedDigits(self, N: int) -> int:
        good_nums = 0
        nums = [x for x in range(N + 1)]
        for x in nums:
            S = str(x)
            good_nums += (all(n not in '347' for n in S)
                         and any(n in '2569' for n in S))
        return good_nums