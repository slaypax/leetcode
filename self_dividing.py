# https://leetcode.com/problems/self-dividing-numbers/submissions/
# A self-dividing number is a number that is divisible by every digit it contains.
# For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0,
# and 128 % 8 == 0.
# Also, a self-dividing number is not allowed to contain the digit zero.
# Given a lower and upper number bound, output a list of every possible self
#  dividing number, including the bounds if possible.


# Runtime: 56 ms
# Your runtime beats 78.01 % of python3 submissions.

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def check_self(n):
            for digit in str(n):
                if digit == '0' or n % int(digit) > 0:  
                    return False    
            return True
               
        nums = [k for (k) in range(left, right + 1) if check_self(k)]
        return(nums)