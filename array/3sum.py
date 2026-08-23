class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        unique_set = set()
        for i in range(len(nums)):
            hm = set()
            for j in range(i + 1, len(nums)):
                third = -(nums[i] + nums[j])
                if third in hm:
                    temp = [nums[i], nums[j], third]
                    temp.sort()
                    unique_set.add(tuple(temp))
                hm.add(nums[j])
        result = [list(triplet) for triplet in unique_set]
        return result