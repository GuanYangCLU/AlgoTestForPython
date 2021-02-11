class Solution:
    """
    @param n: the row of the matrix
    @param m: the column of the matrix
    @param after: the matrix
    @return: restore the matrix
    """
    def matrixRestoration(self, n, m, after):
        # write your code here
        # A B
        # C D
        # D(bf) = D - (B + C - A) = A + D - (B + C)
        # C(bf) = C - A, B(bf) = B - A
        if not after or not len(after[0]):
            return [[]]
        res = [[0 for y in range(len(after[0]))] for x in range(len(after))]
        for i in range(len(after)):
            for j in range(len(after[i])):
                if i == 0 and j == 0:
                    res[i][j] = after[i][j]
                    continue
                if i == 0 and j > 0:
                    res[i][j] = after[i][j] - after[i][j - 1]
                    continue
                if i > 0 and j == 0:
                    res[i][j] = after[i][j] - after[i - 1][j]
                    continue
                res[i][j] = after[i][j] + after[i - 1][j - 1] - (after[i - 1][j] + after[i][j - 1])
        return res
        
