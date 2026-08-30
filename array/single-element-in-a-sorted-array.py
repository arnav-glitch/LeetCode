class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = n - 1
        while l < r:
            m = l + ((r - l) // 2)
            if m % 2 == 0: #m is even
                if m + 1 < n and nums[m] == nums[m + 1]: #left side parity rule follows (singleton in right)
                    l = m + 1
                else: #left side parity rule breaks (singleton in left)
                    r = m
            else: #m is odd
                if m - 1 >= 0 and nums[m] == nums[m - 1]: #left side parity rule follows (singleton in right)
                    l = m + 1
                else:
                    r = m
        return nums[l]