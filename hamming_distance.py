# The Hamming distance between two integers is the number of positions at which
# the corresponding bits are different.
# 0 ≤ x, y < 2**31.

# 36 ms
# Runtime: 39 ms
# slow and uses built ins

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x ^ y).count('1')