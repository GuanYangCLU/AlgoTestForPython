class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dic = {}
        for n in nums:
            dic[n] = dic.get(n, 0) + 1
        return sum(list(map(lambda x: (x * (x - 1)) // 2, dic.values())))
