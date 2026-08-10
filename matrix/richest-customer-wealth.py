class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maximum = 0
        for customer in accounts:
            total = 0
            for rows in customer:
                total += rows
            if total > maximum:
                maximum = total
        return maximum