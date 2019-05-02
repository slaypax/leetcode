# https://leetcode.com/problems/backspace-string-compare
# Runtime: 36 ms, faster than 97.64% of Python3 online submissions for Backspace String Compare.

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def process_string(S):
            processed = []
            for c in S:
                if c != '#':
                    processed.append(c)
                elif c == '#':
                    try:
                        processed.pop()
                    except IndexError:
                        pass
            return "".join(processed)
        return process_string(S) == process_string(T)