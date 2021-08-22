class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        return [sum([self.isInside(xy, query) for xy in points]) for query in queries]
    def isInside(self, xy, query):
        [x1, y1] = xy
        [x2, y2, r] = query
        return 1 if (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2) <= r * r else 0
        
