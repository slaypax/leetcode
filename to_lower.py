# https://leetcode.com/problems/to-lower-case/
# Implement function ToLowerCase() that has a string parameter str, and returns
#  the same string in lowercase.
# Input: "Hello"
# Output: "hello"

# Your runtime beats 74.39 % of python3 submissions.
# Runtime: 36 ms

from string import ascii_lowercase, ascii_uppercase

class Solution:
    def toLowerCase(self, str: str) -> str:
        new_string = []
        for c in str:
            if 'A' <= c <= 'Z':
                 new_string.append(ascii_lowercase[ascii_uppercase.index(c)])
            else:
                 new_string.append(c)
        return "".join(new_string)


# Your runtime beats 74.39 % of python3 submissions
# Runtime: 36 ms

from string import ascii_lowercase, ascii_uppercase

class Solution:
    def toLowerCase(self, str: str) -> str:

        def is_upper(c):
            if 'A' <= c <= 'Z':
                return True
            
        def lower_char(c):
            return ascii_lowercase[ascii_uppercase.index(c)]
        
        new_string = [(lower_char(c)) if is_upper(c) else c for c in str]
        return "".join(new_string)