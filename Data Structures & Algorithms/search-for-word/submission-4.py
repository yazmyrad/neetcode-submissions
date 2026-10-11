class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path = []
        m, n = len(board), len(board[0])
        exists = [False]
        seen = set()
        def dfs(i, j):
            if (i, j) in seen: return
            path.append(board[i][j])
            if word in "".join(path): 
                exists[0] = True
                return
            seen.add((i, j))
            if i+1 < m:
                dfs(i+1, j)

            if i-1 >= 0:
                dfs(i-1, j)

            if j-1 >= 0:
                dfs(i, j-1)

            if j+1 < n: 
                dfs(i, j+1)
            
            path.pop() 
            seen.discard((i, j))   
            return
        dfs(0, 0)
        dfs(m-1, n-1)
        dfs(m-1, 0)
        dfs(0, n-1)
        return exists[0]