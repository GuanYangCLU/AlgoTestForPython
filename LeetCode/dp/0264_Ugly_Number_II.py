class Solution:
    def nthUglyNumber(self, n: int) -> int:
        res = [1]
        idx2 = idx3 = idx5 = 0
        while n > 1:
            nxt = min(res[idx2] * 2, res[idx3] * 3, res[idx5] * 5)
            res.append(nxt)
            n -= 1
            if nxt == res[idx2] * 2:
                idx2 += 1
            if nxt == res[idx3] * 3:
                idx3 += 1
            if nxt == res[idx5] * 5:
                idx5 += 1
        return res[-1]
        
