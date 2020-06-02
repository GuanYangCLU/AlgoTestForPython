class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        row = len(matrix)
        col = len(matrix[0])
        lo, hi = 0, row * col - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            midVal = matrix[mid // col][mid % col]
            if target > midVal:
                lo = mid + 1
            elif target < midVal:
                hi = mid - 1
            else:
                return True  
        return False
        
