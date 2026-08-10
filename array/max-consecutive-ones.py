class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maximum = current = 0
        for i in nums:
            if i == 1:
                current += 1
            else:
                if maximum < current:
                    maximum = current
                current = 0
        if maximum < current:
            maximum = current
        return maximum