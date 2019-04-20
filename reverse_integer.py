# https://leetcode.com/problems/reverse-integer/
# Given a 32-bit signed integer, reverse digits of an integer.
# Assume we are dealing with an environment which could only store integers
# within the 32-bit signed integer range: [−2**31,  2**31 − 1]. 
# returns 0 when the integer overflows.

# Your runtime beats 48.72 % of python3 submissions.home

# Runtime: 56 ms
class Solution:
    def reverse(self, x: int) -> int:
        max = 2**31 - 1
        min = (2* -1)**31
        if x == 0:
            return 0
        
        if x > 0:  
            rev = int("".join([x for x in reversed(str(x))]))
            if rev < max:
                return rev
            else:
                return 0
        if x < 0:
            neg_rev = [x for x in reversed(str(x))]
            neg_rev.pop()
            rev = int("".join(neg_rev)) * -1
            if rev >= min:
                return rev
            else:
                return 0