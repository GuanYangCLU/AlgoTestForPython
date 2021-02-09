class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        prefixSum = self.getPrefixSum(nums)
        for end in range(len(nums) - 1, -1, -1):
            for start in range(end + 1, max(end + 1 - res, -1), -1):
                if prefixSum[end + 1] - prefixSum[start] >= target:
                    length = end + 1 - start
                    res = min(res, length)
                    break
        return 0 if res == float('inf') else res
        
    def getPrefixSum(self, nums):
        prefixSum = [0]
        for n in nums:
            prefixSum.append(prefixSum[-1] + n)
        return prefixSum
