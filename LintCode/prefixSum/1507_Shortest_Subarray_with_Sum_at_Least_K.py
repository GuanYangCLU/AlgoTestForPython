class Solution:
    """
    @param A: the array
    @param K: sum
    @return: the length
    """
    def shortestSubarray(self, A, K):
        # Write your code here.
        res = float('inf')
        prefixSum = self.getPrefixSum(A)
        for end in range(len(A) - 1, -1, -1):
            for start in range(end + 1, max(end + 1 - res, -1), -1):
                if prefixSum[end + 1] - prefixSum[start] >= K:
                    length = end + 1 - start
                    res = min(res, length)
                    break
        return -1 if res == float('inf') else res
        
    def getPrefixSum(self, nums):
        prefixSum = [0]
        for n in nums:
            prefixSum.append(prefixSum[-1] + n)
        return prefixSum
        
