class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        # all posibile: [A, rest of A]
        restNums = nums[::-1]
        for i in range(1, len(nums)):
            nums[i] *= nums[i-1] or 1
            restNums[i] *= restNums[i-1] or 1
        return max(nums + restNums)
        
