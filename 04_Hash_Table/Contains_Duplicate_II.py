class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        positions = {}
        
        for i, num in enumerate(nums):
            if num in positions:
                if i - positions[num] <= k:
                    return True
                else:
                    positions[num] = i
            else:
                positions[num] = i
        return False