# https://leetcode.com/problems/ransom-note/submissions/
# Runtime: 48 ms, faster than 89.67% of Python3 online submissions for Ransom Note.

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        note_count = collections.Counter(ransomNote)
        magazine_count = collections.Counter(magazine)
        check = []
        for letter in ransomNote:
            if letter in magazine:
                if note_count[letter] <= magazine_count[letter]:
                    check.append(letter)
            else:
                return False
        return "".join(check) == ransomNote