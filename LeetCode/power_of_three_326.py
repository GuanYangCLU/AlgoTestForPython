def isPowerOfThree(n):
    if n == 1:
        return True
    elif n < 1:
        return False
    elif n%3 == 0:
        return isPowerOfThree(n/3)
    else:
        return False
n = 45
print(isPowerOfThree(n))

'''
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        elif n < 1:
            return False
        elif n%3 == 0:
            return Solution.isPowerOfThree(self, n/3)
        else:
            return False
p = Solution()
n = 27
p.isPowerOfThree(n)