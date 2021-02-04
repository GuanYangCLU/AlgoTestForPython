class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return 0
        count = 0
        i, j = len(matrix) - 1, 0
        while i >= 0 and j < len(matrix[0]):
            if matrix[i][j] == target:
                count += 1
                i -= 1
                j += 1
                continue
            if matrix[i][j] > target:
                i -= 1
                continue
            j += 1
        return count
        
