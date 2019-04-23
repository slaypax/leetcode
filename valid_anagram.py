# https://leetcode.com/problems/valid-anagram/submissions/
# slow uses sort
# Runtime: 68 ms, faster than 49.99% of Python3 online submissions for Valid Anagram.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(t) == sorted(s)

# faster to use a Counter. Counter is very good and has helped solve a lot of
# these fast.
# Runtime: 44 ms, faster than 94.21% of Python3 online submissions for Valid Anagram.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counter = collections.Counter(s)
        t_counter = collections.Counter(t)
        return s_counter == t_counter



