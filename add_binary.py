# https://leetcode.com/problems/add-binary
#Runtime: 36 ms, faster than 100.00% of Python3 online submissions for Add Binary.

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return str(bin(int(a, 2) + int(b, 2))[2:])