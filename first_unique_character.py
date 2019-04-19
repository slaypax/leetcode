# https://leetcode.com/problems/first-unique-character-in-a-string/
# 
# s = "leetcode"
# return 0.
#
# s = "loveleetcode",
# return 2.


#slow
# Runtime: 184 ms, faster than 21.44% of Python3 online submissions for First Unique Character in a String.
class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        chars = {}
        
        for c in s:
            chars[c] = chars.get(c, 0) + 1
            
        for i, c in enumerate(s):
            if chars[c] == 1:
                return i
        return -1

# built in is faster
# Runtime: 112 ms, faster than 73.05% of Python3 online submissions for First Unique Character in a String.

class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        chars = collections.Counter(s)
            
        for i, c in enumerate(s):
            if chars[c] == 1:
                return i
        return -1


# Runtime: 116 ms, faster than 69.21% of Python3 online submissions for First Unique Character in a String
# not really any faster to use my own or to use enumerate()
class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        chars = collections.Counter(s)
        
        index = 0
        for c in s:
            if chars[c] == 1:
                return index
            else:
                index += 1
            
        return -1