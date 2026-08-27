class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = min_prod = answer = nums[0]
        for i in range(1, len(nums)):
            current = nums[i]
            new_max = max(current, max_prod * current, min_prod * current)
            new_min = min(current, min_prod * current, max_prod * current)
            max_prod = new_max
            min_prod = new_min
            answer = max(answer, new_max)
        return answer        