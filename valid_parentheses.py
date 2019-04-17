# https://leetcode.com/problems/valid-parentheses
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']'
# determine if the input string is valid.
# Input: "()"
# Output: true
# Input: "(]"
# Output: false

# Runtime: 36 ms
# Your runtime beats 86.76 % of python3 submissions.

class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        valid_brackets = {")":"(","]":"[","}":"{"}
        for char in s:
            if char in valid_brackets.values():
                stack.append(char)
            elif char in valid_brackets.keys():
                if stack == [] or valid_brackets[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []