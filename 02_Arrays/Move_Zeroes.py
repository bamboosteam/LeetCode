class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if length == 1: return
        
        write = 0
        for i in range(length):
            if nums[i] != 0:
                nums[write] = nums[i]
                write += 1
                
        nums[write:] = [0] * (length - write)
