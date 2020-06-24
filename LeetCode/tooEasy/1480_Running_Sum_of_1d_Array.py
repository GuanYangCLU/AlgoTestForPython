class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        return nums
        
