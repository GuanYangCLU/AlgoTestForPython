def fib(n):
    if n < 1:
        return 0
    elif n == 1 or n == 2 :
        return 1
    else:
        return fib(n-1) + fib(n-2)
for i in range (1, 20):
    print(i, fib(i))
print(pow(2,31)-1)    

'''    
class Solution:
    def fib(self, N: int) -> int:
        if N < 1:
            return 0
        elif N == 1 or N == 2 :
            return 1
        else:
            return Solution.fib(self, N-1) + Solution.fib(self, N-2)
p = Solution()
N = 5
print(p.fib(N))
'''