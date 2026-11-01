class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        edges = set()
        for j in range(n):
            if board[0][j] == "O": edges.add((0, j))
            if board[m-1][j] == "O": edges.add((m-1, j))
        for i in range(m):
            if board[i][0] == "O": edges.add((i, 0))
            if board[i][n-1] == "O": edges.add((i, n-1))
        
        seen = set()
        def dfs(r, c):
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for x, y in directions:
                nr, nc = r+x, c+y
                if not (0 <= nr < m): continue
                if not (0 <= nc < n): continue
                
                if board[nr][nc] == "O" and (nr, nc) not in seen:
                    seen.add((nr, nc))
                    dfs(nr, nc)
            return
        
        for zero in edges:
            seen.add((zero[0], zero[1]))
            dfs(zero[0], zero[1])

        for i in range(m):
            for j in range(n):
                if (i, j) not in seen and board[i][j] == "O":
                    board[i][j] = "X"
        return
