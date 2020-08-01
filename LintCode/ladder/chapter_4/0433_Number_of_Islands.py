class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        # write your code here
        if not grid or not grid[0]:
            return 0
        
        DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        res = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] and (i, j) not in visited:
                    self.bfs(grid, i, j, visited, DIRECTIONS)
                    res += 1
                    
        return res
        
    def bfs(self, grid, x, y, visited, DIRECTIONS):
        queue = collections.deque([(x, y)])
        visited.add((x, y))
        while queue:
            x, y = queue.popleft()
            for dx, dy in DIRECTIONS:
                next_x, next_y = x + dx, y + dy
                if not self.is_valid(grid, next_x, next_y, visited):
                    continue
                queue.append((next_x, next_y))
                visited.add((next_x, next_y))
                
    def is_valid(self, grid, x, y, visited):
        if not 0 <= x < len(grid) or not 0 <= y < len(grid[0]):
            return False
        if (x, y) in visited:
            return False
        return grid[x][y]
