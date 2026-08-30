class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = end = -1
        n = len(nums)
        l = 0
        r = n - 1
        while l <= r:
            m = l + ((r-l)//2)
            if nums[m] >= target:
                r = m - 1
            else:
                l = m + 1
        if l < n and nums[l] == target:
            start = l
        l = 0
        r = n - 1
        while l <= r:
            m = l + ((r-l)//2)
            if nums[m] <= target:
                l = m + 1
            else:
                r = m - 1
        if r >= 0 and nums[r] == target:
            end = r
        return [start, end]