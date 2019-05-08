# https://leetcode.com/problems/guess-number-higher-or-lower/
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):
# Runtime: 20 ms, faster than 72.00% of Python online submissions for Guess Number Higher or Lower.


class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        lower = 1 
        upper = n
        while lower <= upper:
            mid = (lower + upper) // 2
            if guess(mid) == 0:
                return mid
            elif guess(mid) == -1:
                upper = mid - 1
            elif guess(mid) == 1:
                lower = mid + 1
                