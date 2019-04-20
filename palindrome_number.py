# https://leetcode.com/problems/palindrome-number/

# Runtime: 76 ms, faster than 100.00% of Python3 online submissions for Palindrome Number.
# boomshakalaka

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_2 = x
        return str(x_2)[::-1] == str(x)

# with out turning into string
# (had to look this up, but still converted official solution from c#)
# fails in python3 becuase division is a float
# Runtime: 80 ms, faster than 97.35% of Python online submissions for Palindrome Number.
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reverse_num = 0
        while x > reverse_num:
            reverse_num = reverse_num * 10 + x % 10
            x /= 10
            
        return x == reverse_num or x == reverse_num/10