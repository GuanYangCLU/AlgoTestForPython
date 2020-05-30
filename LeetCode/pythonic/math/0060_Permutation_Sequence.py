class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        res, nums = '', list(range(1, n+1))
        k -= 1 # to get k-1 th next element
        while n > 0:
            n -= 1
            idx, k = divmod(k, math.factorial(n))
            res += str(nums[idx])
            nums.remove(nums[idx])
        return res
        
