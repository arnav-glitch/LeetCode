class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if n < (m * k):
            return -1
        l = min(bloomDay)
        r = max(bloomDay)
        while l < r:
            mid = l + ((r - l)//2)
            count = ans = 0
            for i in range(n):
                if mid >= bloomDay[i]:
                    count += 1
                else:
                    count = 0
                if count == k:
                    ans += 1
                    count = 0
            if ans >= m:
                r = mid
            else:
                l = mid + 1
        return l