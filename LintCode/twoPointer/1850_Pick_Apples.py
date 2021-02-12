class Solution:
    """
    @param A: a list of integer
    @param K: a integer
    @param L: a integer
    @return: return the maximum number of apples that they can collect.
    """
    def PickApples(self, A, K, L):
        # write your code here
        if K + L > len(A):
            return -1
        res = 0
        # K then L
        res = self.findMaxTotal(A, K, L, res)
        res = self.findMaxTotal(A, L, K, res)
        return res
                
    def findMaxTotal(self, nums, leftLen, rightLen, initMax):
        maxTotal = initMax
        for i in range(len(nums) - leftLen - rightLen + 1):
            for j in range(i + leftLen, len(nums) - rightLen + 1):
                total = sum(nums[i:i + leftLen]) + sum(nums[j:j + rightLen])
                maxTotal = max(maxTotal, total)
        return maxTotal
