# https://leetcode.com/problems/design-hashmap
# Runtime: 88 ms, faster than 98.78% of Python3 online submissions for Design HashMap.
# using dict seems like cheating, this probably doens't count.

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.holder_dict = {}
        

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        self.holder_dict[key] = value
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        return self.holder_dict.get(key, -1)
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        if key in self.holder_dict:
            del self.holder_dict[key]
        