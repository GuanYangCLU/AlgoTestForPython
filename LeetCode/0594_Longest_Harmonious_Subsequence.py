class Solution:
    def findLHS(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        dic = {}
        for n in nums:
            dic[n] = dic.get(n, 0) + 1
        # first iterate, get a map that all values as key
        res = 0
        for m in dic:
            if m+1 in dic:
                res = max(res, dic[m] + dic[m+1])
            # no need consider -1 case because we iterate all values it gives
        return res

# Time exceed:
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        dp = [[1, 1] for i in range(len(nums))] # update [+1 len, -1 len]
        dp2 = [1 for i in range(len(nums))]
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                if nums[j] == nums[i]:
                    if dp[i][0] > 1:
                        # already have exactly 1 dif
                        dp[i][0] += 1
                    if dp[i][1] > 1:
                        dp[i][1] += 1
                if nums[j] - nums[i] == 1: # +1 case
                    dp[i][0] += 1
                if nums[j] - nums[i] == -1: # -1 case
                    dp[i][1] += 1
            dp2[i] = max(*dp[i])
        res = max(*dp2)
        return res if res > 1 else 0
