class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res = []
        count = 0
        ele = []
        isCount = True
        for n in nums:
            if isCount:
                count = n
            if not isCount:
                ele = [n]
                res += ele * count
            isCount = not isCount
        return res
        
