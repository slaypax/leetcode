# https://leetcode.com/problems/license-key-formatting/


# Input: S = "2-5g-3-J", K = 2
# Output: "2-5G-3J"

# SLOOOOWWW
# Runtime: 96 ms, faster than 28.03% of Python3 online submissions for License Key Formatting.

from string import ascii_lowercase, ascii_uppercase

class Solution(object):                      
    def licenseKeyFormatting(self, S, K):
        #helper to make lower
        def upper_char(c):
            if 'a' <= c <= 'z':
                return ascii_uppercase[ascii_lowercase.index(c)]
            else:
                return c
        #remove  '-' and make everything upper case then reverse string to handle first 'short' group
        clean_key = ''
        for c in S:
            if c != '-': clean_key += upper_char(c)
        clean_key = clean_key[::-1]
        #make a new key to store answer
        new_key = ''
        #enum the clean_key and add dashes
        for i, c in enumerate(clean_key):         
            if i != 0 and i % K == 0:
                new_key += '-'
            new_key += c
        #straight up flip it and reverse it
        return new_key[::-1]

 class Solution(object):                      
    def licenseKeyFormatting(self, S, K):
        s, lc, uc = '', string.ascii_letters[:26], string.ascii_letters[26:]
        for a in S:
            if a != '-': s += a
        s, ans = s[::-1], ''
        for i, a in enumerate(s):         
            if i != 0 and i % K == 0: ans += '-'
            if a in lc: a = uc[lc.find(a)]
            ans += a
        return ans[::-1]
