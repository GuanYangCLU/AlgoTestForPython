class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix, start = [], n * n + 1 # inside-out reverse spiral
        while start > 1:
            start, end = start - len(matrix), start
            matrix = [[i for i in list(range(start, end))], *[list(j) for j in zip(*matrix[::-1])]] # spiral last level matrix, and put a layer above the matrix
        return matrix
        
