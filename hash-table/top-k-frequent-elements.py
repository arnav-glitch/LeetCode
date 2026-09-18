class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        sort = list(sorted(freq, key=lambda num: freq[num], reverse=True))
        return sort[:k]