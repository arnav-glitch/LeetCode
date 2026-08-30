class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        l = 0
        r = n - 1
        while l < r:
            m = l + ((r - l)//2)
            if nums[m] == target:
                return True
            if nums[l] == nums[m] == nums[r]:
                l += 1
                r -= 1
                continue
            if nums[l] <= nums[m]: #left side is sorted
                if nums[l] <= target <= nums[m]: #left side contains target
                    r = m - 1
                else: #right side contains target
                    l = m + 1
            else: #right side is sorted
                if nums[m] <= target <= nums[r]: #right side contains target
                    l = m + 1
                else: #left side contains target
                    r = m - 1
        return False