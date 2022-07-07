class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def findPattern(s):
            d, ar = {}, []
            idx = 0
            for ch in s:
                if ch not in d.keys():
                    d[ch] = idx
                    idx += 1
                    ar.append(str(idx))
                else:
                    ar.append(str(d[ch]))
            return ar
        return findPattern(s) == findPattern(t)