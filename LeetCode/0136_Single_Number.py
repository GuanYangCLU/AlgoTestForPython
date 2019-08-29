class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = {}
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = [i]
            else: dic[nums[i]].append(i)
        for key in dic.keys():
            if len(dic[key]) == 1:
                return key
