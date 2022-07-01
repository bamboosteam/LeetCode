"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
"""

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        i1, i2 = 0, 0
        nums = []
        if (n1 + n2) % 2 == 0:
            for _ in range((n1 + n2) // 2 + 1):
                if i1 >= n1:
                    nums.append(nums2[i2])
                    i2 += 1
                    continue
                elif i2 >= n2:
                    nums.append(nums1[i1])
                    i1 += 1
                    continue
                if nums1[i1] > nums2[i2]:
                    nums.append(nums2[i2])
                    i2 += 1
                else:
                    nums.append(nums1[i1])
                    i1 += 1
            print(nums)
            return (nums[-1] + nums[-2])/2
        else:
            for _ in range((n1 + n2) // 2 + 1):
                if i1 >= n1:
                    nums.append(nums2[i2])
                    i2 += 1
                    continue
                elif i2 >= n2:
                    nums.append(nums1[i1])
                    i1 += 1
                    continue
                if nums1[i1] > nums2[i2]:
                    nums.append(nums2[i2])
                    i2 += 1
                else:
                    nums.append(nums1[i1])
                    i1 += 1
            return float(nums[-1])
        