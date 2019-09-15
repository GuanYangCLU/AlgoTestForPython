class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        lst = [[0 for j in range (n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    lst[i][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                if lst[i-1][j] != 0 and lst[i][j-1] != 0: 
                    lst[i][j] = lst[i-1][j] + lst[i][j-1]
        return lst[m-1][n-1]
p = Solution()
m = 23
n = 12
print(m,n,p.uniquePaths(m,n))
# for m in range(1,8):
    # for n in range(1,8):
        # print(m,n,p.uniquePaths(m,n))
        
''' 
# recursion, not suitable       
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m <= 1 or n <= 1:
            return 1
        # elif m <= 1 and n > 1:
            # return Solution.uniquePaths(self, m, n-1)
        # elif n <= 1 and m > 1:
            # return Solution.uniquePaths(self, m-1, n)
        elif m > 1 and n > 1:
            return (Solution.uniquePaths(self, m-1, n) + Solution.uniquePaths(self, m, n-1))
p = Solution()
'''
