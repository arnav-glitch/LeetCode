class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hm = {}
        for i in range(len(nums)):
            if nums[i] in hm:
                hm[nums[i]] += 1
                if hm[nums[i]] > 1:
                    return True
            else:
                hm[nums[i]] = hm.get(nums[i], 0) + 1
        return False