class Solution:
    def numSquares(self, n: int) -> int:
        import math
        from collections import deque
        max_sqrt = int(math.sqrt(n))
        sqrts = [i**2 for i in range(1, max_sqrt+1)]
        queue = deque()
        queue.append(n)
        step = 1
        while queue:
            size = len(queue)
            for i in range(size):
                curr = queue.popleft()
                if curr in sqrts: return step
                for i in sqrts:
                    if i > curr: break
                    queue.append(curr - i)
            step += 1