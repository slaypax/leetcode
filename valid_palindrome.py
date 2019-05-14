# https://leetcode.com/problems/valid-palindrome/submissions/
# https://leetcode.com/submissions/detail/228566297/

# slow and you don't really need regex for this.
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        def clean_string(s):
            regex = re.compile(r'[a-zA-Z0-9]')
            cleaned = [x.lower() for x in s if regex.match(x)]
            return cleaned
        cleaned = clean_string(s)
        return cleaned == cleaned[::-1]