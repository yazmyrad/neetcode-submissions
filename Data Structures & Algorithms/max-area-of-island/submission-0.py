class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        area, maxarea = [0], 0
        def dfs(i, j):
            if grid[i][j] == 0: return 
            if grid[i][j] == 1: 
                area[0] += 1
                grid[i][j] = 0
            if i+1 < m:
                dfs(i+1, j)
            if i-1 >= 0:
                dfs(i-1, j)
            if j+1 < n:
                dfs(i, j+1)
            if j-1 >= 0:
                dfs(i, j-1)
            
            return 

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    maxarea = max(maxarea, area[0])
                    area[0] = 0
        return maxarea