class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        for row in matrix:
            if row[-1] < target:
                continue
            else:
                i, j = 0, n
                while i < j:
                    mid = i + (j -i)//2
                    if row[mid] < target:
                        i = mid + 1
                    else:
                        j = mid
                if i < len(row) and row[i] == target:
                    return True
                else:
                    return False
        return False