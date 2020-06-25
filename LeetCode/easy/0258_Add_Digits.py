class Solution:
    def addDigits(self, num: int) -> int:
        def helper(num):
            next, cur = num // 10, num % 10
            if next == 0:
                return num
            while next > 0:
                cur += next % 10
                next //= 10
            return helper(cur)
        return helper(num)
        
