class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rs = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    rs += 4
                    if i > 0 and i < len(grid) - 1:
                        if grid[i-1][j] == 1:
                            rs -= 1
                        if grid[i+1][j] == 1:
                            rs -= 1
                    if i == 0 and i < len(grid) - 1:
                        if grid[i+1][j] == 1:
                            rs -= 1
                    if i == len(grid) - 1 and i > 0:
                        if grid[i-1][j] == 1:
                            rs -= 1
                    if j > 0 and j < len(grid[i]) - 1:
                        if grid[i][j-1] == 1:
                            rs -= 1
                        if grid[i][j+1] == 1:
                            rs -= 1
                    if j == 0 and j < len(grid[i]) - 1:
                        if grid[i][j+1] == 1:
                            rs -= 1
                    if j == len(grid[i]) - 1 and j > 0:
                        if grid[i][j-1] == 1:
                            rs -= 1
        return rs
