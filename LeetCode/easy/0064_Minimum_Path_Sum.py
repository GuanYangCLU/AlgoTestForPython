class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not len(grid) or not len(grid[0]):
            return 0
        res = grid[:]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    continue
                elif i == 0 and j != 0:
                    res[i][j] += res[i][j-1]
                elif j == 0 and i != 0:
                    res[i][j] += res[i-1][j]
                else:
                    res[i][j] += min(res[i-1][j], res[i][j-1])
        return res[len(grid) - 1][len(grid[0]) - 1]
        
