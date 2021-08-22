class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        res = [first]
        cur = first
        for n in encoded:
            cur ^= n
            res.append(cur)
        return res
        
