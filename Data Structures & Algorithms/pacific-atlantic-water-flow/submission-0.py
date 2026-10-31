class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        seen = set()
        pacific, atlantic = [False], [False]
        def dfs(r, c):            
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for x, y in directions:
                nr, nc = r+x, c+y
                if (nr, nc) in seen:
                    continue
                if not (0 <= nr < m and 0 <= nc < n):
                    if nr < 0 or nc < 0:
                        pacific[0] = True
                    elif nr >= m or nc >= n:
                        atlantic[0] = True
                    continue
                
                if heights[nr][nc] <= heights[r][c]:
                    seen.add((nr, nc))
                    dfs(nr, nc)

            return
        ans = []
        for i in range(m):
            for j in range(n):
                dfs(i, j)
                if pacific[0] and atlantic[0]:
                    ans.append([i, j])

                pacific, atlantic = [False], [False]
                seen = set()
        return ans