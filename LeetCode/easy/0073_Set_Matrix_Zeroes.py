class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        set_i, set_j = set(), set()
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    set_i.add(i)
                    set_j.add(j)
        for index_i in set_i:
            matrix[index_i] = [0] * n
        for index_j in set_j:
            for i in range(m):
                matrix[i][index_j] = 0
        return matrix
