# solution 1 - bfs

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        from collections import deque
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        m, n = len(grid), len(grid[0])
        ans = 0
        queue = deque()
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    ans += 1
                    grid[i][j] = '0'
                    queue.append([i, j])
                    # traverse the island by bfs
                    while queue:
                        start = queue.popleft()
                        col, row = start[0], start[1]
                        for direction in directions:
                            c, r = col + direction[0], row + direction[1]
                            if c < 0 or r < 0 or c >= m or r >= n or grid[c][r] == "0":
                                continue
                            grid[c][r] = "0"
                            queue.append([c, r])
        return ans


# solition 2 - recursion (inclusive dfs)

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid: List[List[str]], r: int, c: int):
            nr = len(grid)
            nc = len(grid[0])

            if r < 0 or c < 0 or r >= nr or c >= nc or grid[r][c] == "0":
                return

            grid[r][c] = "0"
            dfs(grid, r-1, c)
            dfs(grid, r+1, c)
            dfs(grid, r, c-1)
            dfs(grid, r, c+1)
            
        if grid == None or len(grid) == 0: return 0
        
        nr = len(grid)
        nc = len(grid[0])
        count = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    count += 1
                    dfs(grid, r, c)
        return count