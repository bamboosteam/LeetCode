"""
You are given an integer array nums where the largest integer is unique.

Determine whether the largest element in the array is at least twice as much as every other number in the array. If it is, return the index of the largest element, or return -1 otherwise.
"""

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        largest = [0, nums[0]]
        second_largest = [-1, -1]

        for i, num in enumerate(nums):
            if num > largest[1]:
                second_largest = largest
                largest = [i, num]
            elif num > second_largest[1] and num < largest[1]:
                second_largest = [i, num]
        
        if largest[1] >= second_largest[1]*2: return largest[0]
        else: return -1
