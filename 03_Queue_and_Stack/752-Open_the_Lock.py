class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends: return -1
        from collections import deque
        def next_move(slot: str) -> List[str]:
            for i in range(4):
                x = int(slot[i])
                for d in (-1, 1):
                    y = (x + d) % 10
                    yield slot[:i] + str(y) + slot[i+1:]
        queue, visited = deque(), set()
        step = 0
        # initialize
        queue.append("0000")
        visited.add("0000")
        # BFS
        while queue:
            size = len(queue)
            for i in range(size):
                curr = queue.popleft()
                if curr == target: return step
                if curr in deadends: continue
                for slot in next_move(curr):
                    if slot not in visited:
                        queue.append(slot)
                        visited.add(slot)
            step += 1
        return -1