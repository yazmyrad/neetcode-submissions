class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = [num for num in board[i] if num.isdigit()]
            col = [hor[i] for hor in board if hor[i].isdigit()]
            
            if len(set(row)) != len(row): return False
            if len(set(col)) != len(col): return False
        hashset = defaultdict(list)
        for i in range(9):
            for j in range(9):
                if board[i][j].isdigit():
                    hashset[int(j/3)*3+int(i/3)].append(int(board[i][j]))  
        for values in hashset.values():
            if len(set(values)) != len(values):
                return False
        return True