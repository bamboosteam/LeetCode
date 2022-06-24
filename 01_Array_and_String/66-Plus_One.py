class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        if digits[-1] != 10:
            return digits
        
        idx = len(digits) - 1
        while digits[idx] == 10:
            if idx == 0:
                break
            digits[idx] = 0
            digits[idx - 1] += 1
            idx -= 1
        
        if digits[0] == 10:
            digits[0] = 0
            return [1] + digits
        
        return digits
        