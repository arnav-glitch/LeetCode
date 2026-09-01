class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        l = 1
        r = max(nums)
        while l < r:
            m = l + ((r-l)//2)
            total = 0
            for i in range(n):
                total += -(-nums[i]//m)
            if total <= threshold:
                r = m
            else:
                l = m + 1
        return r