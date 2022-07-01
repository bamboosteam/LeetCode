"""
Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.

In one move, you can increment or decrement an element of the array by 1.

Test cases are designed so that the answer will fit in a 32-bit integer.
"""

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        import statistics
        ave = int(statistics.median(nums))
        result = 0
        for i in nums:
            result += abs(ave - i)

        return result

# solution without median
# Algorithm

# In the previous approach, we went for finding the median after sorting and then calculated the number of moves required. 
# But, if we observe properly, we'll find that if the array is sorted, we can do the same task without actually finding the median or the number kk to which we need to settle at the end. 
# To proceed with this, let's look at the maximum(maxmax) and the minimum numbers(minmin) in the array, which currently lie at its extreme positions. We know, at the end, both these numbers should be equalized to kk. 
# For the number maxmax, the number of moves required to do this is given by max - kmax−k. 
# Similarly, for the number minmin, the number of moves is given by k - mink−min. Thus, the total number of moves for both maxmax and minmin is given by max - k + (k - min) = max - minmax−k+(k−min)=max−min, which is independent of the number kk. 
# Thus, we can continue now, with the next maximum and the next minimum number in the array, until the complete array is exhausted.



class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        le, ri = 0, len(nums) - 1
        result = 0
        while le < ri:
            result += abs(nums[ri] - nums[le])
            le += 1
            ri -= 1
        return result
            