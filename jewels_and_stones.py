# https://leetcode.com/problems/jewels-and-stones/
# You're given strings J representing the types of stones that are jewels
#  and S representing the stones you have.  Each character in S is a type 
# of stone you have.  You want to know how many of the stones you have 
# are also jewels.
# Input: J = "aA", S = "aAAbbbb"
# Output: 3

# Your runtime beats 99.68 % of python3 submissions.
# Runtime: 36 ms

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewels = 0
        for stone in S:
            if stone in J:
                jewels += 1
        return jewels