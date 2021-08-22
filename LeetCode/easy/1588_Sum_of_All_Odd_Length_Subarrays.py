class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        res = 0
        for half in range((len(arr) + 1) // 2):
            res += self.getSumByLength(2 * half + 1, arr)
        return res
        
    def getSumByLength(self, l, arr):
        res = 0
        for i in range(len(arr) - l + 1):
            res += sum(arr[i : i + l])
        return res
        
