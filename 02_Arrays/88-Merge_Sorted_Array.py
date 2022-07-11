class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0: return
        elif m == 0:
            nums1[:n] = nums2[:n]
            return
        length = n + m - 1
        for i in range(length, -1, -1):
            if n == 0:
                break
            elif m == 0:
                nums1[:n] = nums2[:n]
                break
            elif nums1[m - 1] <= nums2[n - 1]:
                nums1[i] = nums2[n - 1]
                n -= 1
            else:
                nums1[i] = nums1[m - 1]
                m -= 1
            