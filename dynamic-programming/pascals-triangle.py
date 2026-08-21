class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows = [[1]]
        previous = [1]
        for i in range(1, numRows):
            current = []
            current.append(1)
            for j in range(1, i):
                current.append(previous[j] + previous[j-1])
            current.append(1)
            rows.append(current)
            previous = current
        return rows