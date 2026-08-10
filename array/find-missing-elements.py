class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        mySet = set()
        for n in nums:
            mySet.add(n)
        max_element = max(nums)
        min_element = min(nums)
        missing_nums = []
        for i in range(min_element, max_element + 1):
            if i not in mySet:
                missing_nums.append(i)
        return missing_nums