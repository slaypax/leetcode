# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/submissions/
# Runtime: 32 ms, faster than 99.68% of Python3 online submissions for Two Sum II - Input array is sorted.

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low = 0
        high = len(numbers) - 1
        while low < high:
            two_sum = numbers[low] + numbers[high]
            if two_sum == target: 
                return low + 1, high + 1
            elif two_sum < target:
                low += 1
            else:
                high -= 1
                
        return -1, -1