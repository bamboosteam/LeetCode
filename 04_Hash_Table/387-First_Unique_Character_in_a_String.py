class Solution:
    def firstUniqChar(self, s: str) -> int:
        count, found = {}, set()
        for i in range(len(s)):
            if s[i] in found:
                continue
            elif s[i] in count:
                found.add(s[i])
                count.pop(s[i])
            else:
                count[s[i]] = i
        
        if not count:
            return -1
        else:
            return min(count.values())
        
        