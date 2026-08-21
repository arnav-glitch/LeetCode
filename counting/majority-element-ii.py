class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidate1 = None
        candidate2 = None
        count1 = count2 = 0
        for i in range(len(nums)):
            if nums[i] == candidate1:
                count1 += 1
            elif nums[i] == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1 = nums[i]
                count1 += 1
            elif count2 == 0:
                candidate2 = nums[i]
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        n = len(nums)//3
        count1 = count2 = 0
        for i in range(len(nums)):
            if nums[i] == candidate1:
                count1 += 1
            elif nums[i] == candidate2:
                count2 += 1
            else:
                continue
        if count1 > n and count2 > n:
            return [candidate1, candidate2]
        elif count1 > n:
            return [candidate1]
        elif count2 > n:
            return [candidate2]
        else:
            return []