class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        if not time:
            return 0
        dic = {}
        res = 0
        for t in time:
            matchedKey = (60 - t % 60) % 60
            res += dic.get(matchedKey, 0)
            dic[t % 60] = dic.get(t % 60, 0) + 1
        return res
        
