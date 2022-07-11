class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = len(nums)

        if length == 0:
            return 0
        elif length == 1 and nums[0] != val:
            return 1
        
        # find ri
        le, ri = 0, -1
        
        for i in range(length - 1, -1, -1):
            if nums[i] != val:
                ri = i
                break
        
        if ri == -1:
            return 0
        
        # in-place remove
        while le < ri:
            print(nums, le, ri)
            if nums[le] == val:
                nums[le], nums[ri] = nums[ri], nums[le]
                le += 1
                # move to next not val index
                while nums[ri] == val:
                    ri -= 1
            else:
                le += 1
        count = 0
        
        for i in range(length-1, -1, -1):
            if nums[i] == val:
                count += 1
            else:
                break
        return length - count