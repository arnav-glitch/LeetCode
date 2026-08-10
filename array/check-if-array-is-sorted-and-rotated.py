class Solution:
    def check(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        violations = i = 0
        while i+1 < len(nums):
            if violations >= 2:
                return False
            else:
                if nums[i+1] < nums[i]:
                    violations += 1
            i += 1
        if nums[-1] > nums[0]:
            violations += 1
        return violations <= 1