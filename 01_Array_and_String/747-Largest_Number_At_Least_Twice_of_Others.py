"""
You are given an integer array nums where the largest integer is unique.

Determine whether the largest element in the array is at least twice as much as every other number in the array. If it is, return the index of the largest element, or return -1 otherwise.
"""

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        ans, tmpMax = 0, nums[0]

        for i, x in enumerate(nums):
            if x >= tmpMax*2:
                ans, tmpMax = i, x

        nums.sort()
        if tmpMax == nums[-1] and tmpMax >= nums[-2]*2:
            return ans
        else:
            return -1
