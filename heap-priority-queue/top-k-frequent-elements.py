class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        hm = {}
        for i in range(len(nums)):
            hm[nums[i]] = hm.get(nums[i], 0) + 1
        sorted_hm = dict(sorted(hm.items(), key=lambda x: x[1], reverse = True))
        result = []
        for key, value in sorted_hm.items():
            result.append(key)
            k -= 1
            if k == 0:
                break
        return result