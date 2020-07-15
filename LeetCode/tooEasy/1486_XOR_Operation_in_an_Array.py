class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        res = 0
        for i in range(start, start + 2 * (n - 1) + 1, 2):
            res ^= i
        return res
        
