class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        resMax = curMax = prevMax = nums[0]
        for i in range(1, len(nums)):
            curMax = max(nums[i], prevMax + nums[i])
            resMax = max(curMax, resMax)
            prevMax = curMax
            
        return resMax
