"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1: return len(nums)
        nums.sort()
        result = [nums[0]]
        max_len = 0
        for num in nums:
            if num == result[-1]:
                continue
            elif num == result[-1] + 1:
                result.append(num)
            else:
                max_len = max(len(result), max_len)
                result = [num]
        max_len = max(len(result), max_len)
        return max_len