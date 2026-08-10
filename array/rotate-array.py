class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        def reverse_array(arr, start, stop):
            while start < stop:
                arr[start], arr[stop] = arr[stop], arr[start]
                start += 1
                stop -= 1
        reverse_array(nums, 0, len(nums) - k - 1)
        reverse_array(nums, len(nums) - k, len(nums) - 1)
        reverse_array(nums, 0, len(nums) - 1) 
        
