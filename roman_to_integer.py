# https://leetcode.com/problems/roman-to-integer/

# Given a roman numeral, convert it to an integer. Input is guaranteed to be
# within the range from 1 to 3999

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_nums = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        # break the rulse cuz it's easier to solve this problem with a simple
        # dict lookup
        int_rep = 0
        s = s.replace('IV', "IIII")
        s = s.replace("IX", "VIIII")
        s = s.replace('XL', "XXXX")
        s = s.replace("XC", "LXXXX")
        s = s.replace('CD', "CCCC")
        s = s.replace("CM", "DCCCC")
        for rn in s:
            int_rep += roman_nums[rn]
        return int_rep
        