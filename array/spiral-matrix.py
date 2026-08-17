class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1
        result = []
        while top <= bottom and left <= right:
            i = left
            j = right
            while i <= j:
                result.append(matrix[top][i])
                i += 1
            top += 1
            i = top
            j = bottom
            while i <= j:
                result.append(matrix[i][right])
                i += 1
            right -= 1
            if top <= bottom:
                i = left
                j = right
                while j >= i:
                    result.append(matrix[bottom][j])
                    j -= 1
                bottom -= 1
            if left <= right:
                i = top
                j = bottom
                while j >= i:
                    result.append(matrix[j][left])
                    j -= 1
                left += 1
        return result