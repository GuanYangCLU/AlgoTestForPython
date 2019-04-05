class Solution:
    def pos(self, x):
        if x < 10:
            return 0
        else:
            return Solution.pos(self,x//10) + 1
    def helper(self, x):
        if x < 0:
            return -(Solution.helper(self,-x))
        elif x < 10:
            return x
        else:
            return (x%10)*pow(10, Solution.pos(self,x)) + Solution.helper(self,x//10)
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if Solution.helper(self,x) < -pow(2,31) or Solution.helper(self,x) > pow(2,31)-1:
            return 0
        else:
            return Solution.helper(self,x)
p = Solution()
x = 157
p.reverse(x)