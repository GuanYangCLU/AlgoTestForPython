class Solution:
    """
    @param nums: a list of integer
    @param k: an integer
    @return: return an integer, denote the minimum length of continuous subarrays whose sum equals to k
    """
    def subarraySumEqualsKII(self, nums, k):
        # write your code here
        res = float('inf')
        prefixSum = self.getPrefixSum(nums)
        mapSumToIndex = { 0: 0 }
        for end in range(len(nums)):
            maybeSumAsStart = prefixSum[end + 1] - k
            if maybeSumAsStart in mapSumToIndex:
                length = end + 1 - mapSumToIndex[maybeSumAsStart]
                res = min(res, length)
            mapSumToIndex[prefixSum[end + 1]] = end + 1
        return -1 if res == float('inf') else res
        
    def getPrefixSum(self, nums):
        prefixSum = [0]
        for n in nums:
            prefixSum.append(prefixSum[-1] + n)
        return prefixSum
        
