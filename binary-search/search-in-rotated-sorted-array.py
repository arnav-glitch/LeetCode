class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n - 1
        while l <= r:
            m = l + ((r - l)//2)
            if nums[m] == target: #current value of m matches target, return and stop
                return m
            if nums[l] <= nums[m]: #left half is sorted
                if nums[l] <= target <= nums[m]: #target is in left half
                    r = m - 1
                else: #target is in right half
                    l = m + 1
            else: #right half is sorted
                if nums[m] <= target <= nums[r]: #target is in right half
                    l = m + 1
                else: #target is in left half
                    r = m - 1
        return -1