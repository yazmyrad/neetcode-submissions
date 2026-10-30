class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                if grid[i][j] == 1:
                    fresh += 1

        minutes = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while q:
            k = len(q)
            for _ in range(k):
                i, j = q.popleft()
                for x, y in directions:
                    if (i+x) in range(m) and (j+y) in range(n) and grid[i+x][j+y] == 1:
                        grid[i+x][j+y] = 2
                        fresh -= 1
                        q.append((i+x, j+y))

            minutes += 1 if q else 0

        return minutes if fresh == 0 else -1