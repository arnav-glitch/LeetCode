class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        current_sum = 0
        total_sum = 0
        prefix_sum = { 0 : 1 }
        for n in nums:
            current_sum += n
            difference = current_sum - k
            total_sum += prefix_sum.get(difference, 0)
            prefix_sum[current_sum] = 1 + prefix_sum.get(current_sum, 0)
        return total_sum