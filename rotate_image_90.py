# https://leetcode.com/problems/rotate-image/

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix_length = len(matrix[0])
        for i in range(matrix_length):
            for j in range(i, matrix_length):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
                
        for i in range(matrix_length):
            matrix[i].reverse()