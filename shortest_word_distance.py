# https://leetcode.com/problems/shortest-word-distance
# Given a list of words and two words word1 and word2,
# return the shortest distance between these two words in the list.

class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        The distance between any two postions i1 and i2 is |i1- i2|. is that we need to find all occurences of i1 and i2 and  
        check if |i1-i2| is less than the minimum distance computed so far
        """
        size = len(words)
        i1, i2 = size, size
        min_dist = size
        
        for i in range(size):
            if words[i] == word1:
                i1 = i 
                min_dist = min(min_dist, abs(i1 - i2))
            elif words[i] == word2:
                i2 = i
                min_dist = min(min_dist, abs(i1 - i2))
        return min_dist