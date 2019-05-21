# https://leetcode.com/problems/reverse-words-in-a-string-iii/
# https://leetcode.com/submissions/detail/230092671/

class Solution:
    def reverseWords(self, s: str) -> str:
        
        def get_words(string):
            return string.split(" ")
        
        def reverse_word(string):
            return string[::-1]
        
        return " ".join([reverse_word(x) for x in get_words(s)])