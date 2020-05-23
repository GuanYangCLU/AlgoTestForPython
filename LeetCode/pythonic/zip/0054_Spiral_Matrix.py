# https://leetcode.com/problems/spiral-matrix/discuss/20571/1-liner-in-Python-%2B-Ruby
# 边削边转
# classic usage of zip: wrap column as row
# why matrix.pop(0) is turple?

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not len(matrix):
            return []
        return [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])
        
