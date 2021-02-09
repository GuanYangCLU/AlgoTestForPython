class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefixSum = self.getPrefixSum(nums)
        mapSumToIndexes = { 0: [0] }
        for end in range(len(nums)):
            maybeSumAsStart = prefixSum[end + 1] - k
            if maybeSumAsStart in mapSumToIndexes:
                count += len(mapSumToIndexes[maybeSumAsStart])
            mapSumToIndexes[prefixSum[end + 1]] = mapSumToIndexes.get(prefixSum[end + 1], []) + [end + 1]
        return count
        
    def getPrefixSum(self, nums):
        prefixSum = [0]
        for n in nums:
            prefixSum.append(prefixSum[-1] + n)
        return prefixSum
