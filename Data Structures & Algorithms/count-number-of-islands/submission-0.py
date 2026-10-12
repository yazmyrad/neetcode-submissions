class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        cnt = 0
        def dfs(i, j):
            if grid[i][j] == "0": return 
            if grid[i][j] == "1": 
                grid[i][j] = "0"
            #print(i, j, grid[i][j])
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
                if grid[i][j] == "1":
                    dfs(i, j)
                    cnt += 1
        return cnt