class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans = float('inf')
        n = len(nums)
        l = 0
        r = n - 1
        while l <= r:
            m = l + ((r - l)//2)
            if nums[l] <= nums[m]: #if the left half is sorted, take the min and eliminate left
                ans = min(ans, nums[l])
                l = m + 1
            else:
                ans = min(ans, nums[m])
                r = m - 1
        return ans