class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        b_val = bin(n)
        s_val = str(b_val)[2:]
        for i in range(len(s_val)-1):
            if s_val[i] == s_val[i+1]:
                return False
        return True
