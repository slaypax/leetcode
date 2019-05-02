# Runtime: 40 ms, faster than 86.89% of Python3 online submissions for Most Common Word.

import re
import operator

regex = ('\w*\w')

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # regex to match words
        words = re.findall(regex, paragraph)
        # make all words lower case
        for i in range(len(words)):
            words[i] = words[i].lower()
        # count all the words
        words_map = collections.Counter(words)
        # remove banned words from the map
        for banned_word in banned:
            try:
                del words_map[banned_word]
            except:
                pass
        # return most common element
        return(words_map.most_common(1)[0][0])