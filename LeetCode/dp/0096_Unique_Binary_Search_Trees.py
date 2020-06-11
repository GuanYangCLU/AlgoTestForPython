class Solution:
    def numTrees(self, n: int) -> int:
        # a(i) = sigma: a(x) * a(n-x-1) (x: 0~i-1)
        res = [0] * (n+1)
        res[0] = 1
        for i in range(1, n+1):
            for j in range(i):
                res[i] += res[j] * res[i-j-1]
        return res[n]
