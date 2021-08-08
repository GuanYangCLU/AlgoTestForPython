DIRECTIONS = [(1, 0), (-1, 0), (0, -1), (0, 1)]

class Solution:
    def __init__(self):
        self.size = 0
        self.fathers = {}
        
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        res = []
        islands = set()
        for pos in positions:
            x, y = pos[0], pos[1]
            if (x, y) in islands:
                # dup add
                res.append(self.size)
                continue
            self.size += 1
            self.fathers[(x, y)] = (x, y)
            islands.add((x, y))
            can_link_area = [(x + dx, y + dy) for (dx, dy) in DIRECTIONS]
            
            for can_link_pos in can_link_area:
                if can_link_pos in islands:
                    # should be linked
                    self.union((x, y), can_link_pos)
            res.append(self.size)
            
        return res
    
    def union(self, pos_a, pos_b):
        father_a = self.find(pos_a)
        father_b = self.find(pos_b)
        # print(pos_a, pos_b, father_a, father_b)
        if father_a != father_b:
            self.fathers[father_a] = father_b
            self.size -= 1
            
    def find(self, pos):
        path = []
        cur = pos
        while cur != self.fathers[cur]:
            path.append(cur)
            cur = self.fathers[cur]
            
        for child in path:
            self.fathers[child] = cur
        return cur
        
