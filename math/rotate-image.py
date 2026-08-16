class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if j > i:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        i = 0
        while i < len(matrix):
            left = 0
            right = len(matrix[i]) - 1
            while left < right:
                matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]
                left += 1
                right -= 1
            i += 1