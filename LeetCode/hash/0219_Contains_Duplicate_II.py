class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k < 1:
            return False
        dic = {}
        cur, resMin = len(nums), len(nums)
        for i in range(len(nums)):
            if nums[i] in dic:
                cur = i - dic[nums[i]]
                resMin = min(cur, resMin)
                if resMin <= k and resMin < len(nums):
                    return True
            dic[nums[i]] = i
