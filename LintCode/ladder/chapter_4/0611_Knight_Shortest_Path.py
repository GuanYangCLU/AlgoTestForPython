"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path 
    """
    def shortestPath(self, grid, source, destination):
        # write your code here
        if not grid or not grid[0]:
            return -1
        if grid[source.x][source.y] or grid[destination.x][destination.y]:
            return -1
        if (source.x, source.y) == (destination.x, destination.y):
            return 0
        
        DIRECTIONS = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
        return self.bfs(grid, source, destination, DIRECTIONS)
        
    def bfs(self, grid, source, destination, DIRECTIONS):
        start_x, start_y = source.x, source.y
        queue = collections.deque([(start_x, start_y)])
        distance = { (start_x, start_y): 0 }
        while queue:
            x, y = queue.popleft()
            for dx, dy in DIRECTIONS:
                new_x, new_y = x + dx, y + dy
                if (new_x, new_y) == (destination.x, destination.y):
                    return distance[(x, y)] + 1
                if not self.is_valid(grid, new_x, new_y, distance):
                    continue
                queue.append((new_x, new_y))
                distance[(new_x, new_y)] = distance[(x, y)] + 1
        return -1
        
    def is_valid(self, grid, x, y, distance):
        if not 0 <= x < len(grid) or not 0 <= y < len(grid[0]):
            return False
        if (x, y) in distance:
            return False
        return not grid[x][y]
        
