class Solution:
    def isValid(self, s: str) -> bool:
        pair = {'(':')', "[":']', '{':'}'}
        opener = ['(', '[', '{']
        stack = []
        for i in s:
            if i in opener: 
                stack.append(i)
            else:
                if not stack: return False
                elif pair[stack[-1]] == i:
                    stack.pop()
                else:
                    return False
        return not stack