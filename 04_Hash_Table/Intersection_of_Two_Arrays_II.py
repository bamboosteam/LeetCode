class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1, ans = {}, []
        
        for num in nums1:
            if num in count1:
                count1[num] += 1
            else:
                count1[num] = 1
        
        for num in nums2:
            if num in count1 and count1[num] >= 1:
                ans.append(num)
                count1[num] -= 1
        
        return ans
        