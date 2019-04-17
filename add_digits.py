# https://leetcode.com/problems/add-digits/
# Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

# 40 ms
# Your runtime beats 99.77 % of python3 submissions.
# https://en.wikipedia.org/wiki/Digital_root#Congruence_formula

class Solution:
    def addDigits(self, num: int) -> int:
        return 1 + ((num - 1) % 9) if num else 0