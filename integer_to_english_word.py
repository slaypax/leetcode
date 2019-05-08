# https://leetcode.com/problems/integer-to-english-words/
# Runtime: 24 ms, faster than 99.47% of Python online submissions for Integer to English Words

class Solution(object):
    def __init__(self):
        self.integers = [1000000000, 1000000, 1000, 100, 90, 80, 70, 60, 50, 40, 30, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        self.english_words = ["Billion", "Million", "Thousand", "Hundred", "Ninety", "Eighty", "Seventy", "Sixty", "Fifty", "Forty", "Thirty", "Twenty", "Nineteen", "Eighteen", "Seventeen", "Sixteen", "Fifteen", "Fourteen", "Thirteen", "Twelve", "Eleven", "Ten", "Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One" ]
        self.result = []
        
    def numberToWords(self, num):
        if num == 0:
            return "Zero"
        
        self.converter(num)
        return " ".join(self.result)

    def converter(self, num):
        for i in range(len(self.integers)):
            if num >= self.integers[i]:
                if num >= 100:
                    self.converter((num / self.integers[i]))
                    self.result.append(self.english_words[i])
                    self.converter((num % self.integers[i]))
                else:
                    self.result.append(self.english_words[i])
                    self.converter((num - self.integers[i]))
                break
