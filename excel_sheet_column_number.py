class Solution:
    def titleToNumber(self, s: str) -> int:
        row = 0
        multiplier = 1
        for c in s[::-1]:
            row += (ord(c) - 64) * multiplier
            multiplier *= 26
        return row