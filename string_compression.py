# https://leetcode.com/problems/string-compression/
#
# Given an array of characters, compress it in-place.
# The length after compression must always be smaller than or equal to the original array.
# Every element of the array should be a character (not int) of length 1.
# After you are done modifying the input array in-place, return the new length of the array.

# not finished

class OrderedCounter(collections.Counter, collections.OrderedDict):
    'Counter that remembers the order elements are first encountered'

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, collections.OrderedDict(self))

    def __reduce__(self):
        return self.__class__, (collections.OrderedDict(self),)

class Solution:
    def compress(self, chars: List[str]) -> int:
        ordered_array_count = OrderedCounter(chars)
            