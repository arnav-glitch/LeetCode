class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        j = 0
        k = 1
        for i in range(len(nums)):
            if nums[i] > 0:
                result[j] = nums[i]
                j += 2
            else:
                result[k] = nums[i]
                k += 2
        return result