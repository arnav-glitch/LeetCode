class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        l, r = 1, max(piles)
        while l < r:
            m = l + ((r-l)//2)
            hour = 0
            for pile in piles:
                hour += -(-pile//m)
                if hour > h:
                    break
            if hour <= h:
                r = m
            else:
                l = m + 1
        return r