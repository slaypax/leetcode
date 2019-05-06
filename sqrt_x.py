# https://leetcode.com/problems/sqrtx/
# Runtime: 44 ms, faster than 91.90% of Python3 online submissions for Sqrt(x).

class Solution:
    def mySqrt(self, x: int) -> int:
        lower = 0
        upper = x
        
        while lower <= upper:
            mid = (lower + upper) // 2
            if mid * mid <= x < (mid + 1) * (mid + 1):
                return mid
            if mid * mid > x:
                upper = mid - 1
            else:
                lower = mid + 1