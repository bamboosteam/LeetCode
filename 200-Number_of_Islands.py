class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        m, n = len(grid), len(grid[0])
        ans = 0
        queue = []
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    ans += 1
                    grid[i][j] = '0'
                    queue.append([i, j])
                    # traverse the island by bfs
                    while queue:
                        start = queue.pop(0)
                        col, row = start[0], start[1]
                        for direction in directions:
                            c, r = col + direction[0], row + direction[1]
                            if c < 0 or r < 0 or c >= m or r >= n or grid[c][r] == "0":
                                continue
                            grid[c][r] = "0"
                            queue.append([c, r])
        return ans