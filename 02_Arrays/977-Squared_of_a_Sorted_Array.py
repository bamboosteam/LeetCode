class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        le, ri = 0, n - 1
        for i in range(n - 1, -1, -1):
            if abs(nums[le]) < abs(nums[ri]):
                square = nums[ri]
                ri -= 1
            else:
                square = nums[le]
                le += 1
            ans[i] = square ** 2
        return ans