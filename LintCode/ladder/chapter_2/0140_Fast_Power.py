class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """
    def fastPower(self, a, b, n):
        # write your code here
        if b == 0:
            return
        if a == 0:
            return 0
        if n == 0:
            return 1 if b != 1 else 0
            
        a = a % b
        res = 1
        while n > 0:
            # n / 2 个 a**2 看是否余一项
            if n % 2 == 1:
                res = (res * a) % b
            a = (a * a) % b
            n = n // 2
        
        return res
