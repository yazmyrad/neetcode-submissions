class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2**31 - 1
        m, n = len(grid), len(grid[0])
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i, j))

        visited = set()
        while q:
            cell = q.popleft()
            visited.add(cell)
            
            i, j = cell
            directions = [(i, j+1), (i, j-1), (i+1, j), (i-1, j)]
            for x, y in directions:
                if (x, y) in visited:
                    continue
                if x in range(m) and y in range(n):
                    if grid[x][y] == INF:
                        grid[x][y] = grid[i][j] + 1
                        q.append((x, y))

        return