class Solution:
    def minPartitions(self, n: str) -> int:
        res = 0
        for c in n:
            res = max(int(c), res)
        return res
        
