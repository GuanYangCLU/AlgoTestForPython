class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """
    def twoSum6(self, nums, target):
        # write your code here
        if not nums or len(nums) < 2:
            return 0
            
        nums.sort()
        left, right = 0, len(nums) - 1
        res = 0
        
        while left < right:
            if left > 0 and nums[left] == nums[left - 1]:
                left += 1
                continue
            if right < len(nums) - 1 and nums[right] == nums[right + 1]:
                right -= 1
                continue
            if nums[left] + nums[right] == target:
                res += 1
                left += 1
                right -= 1
                continue
            if nums[left] + nums[right] > target:
                right -= 1
                continue
            if nums[left] + nums[right] < target:
                left += 1
        
        return res
