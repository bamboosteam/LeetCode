class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        
        n = len(arr)
        z = 0
        
        # Decide final point
        for left in range(n):
            if left > n - 1 - z:
                break
                
            if arr[left] == 0:
                if left == n - 1 - z:
                    arr[-1] = 0
                    n = n - 1
                    break
                z += 1
        
        
        # in-place process
        idx = n - 1
        while idx > 0:
            if arr[idx - z] == 0:
                arr[idx], arr[idx - 1] = 0, 0
                z -= 1
                idx -= 1
            else:
                arr[idx] = arr[idx - z]
            idx -= 1