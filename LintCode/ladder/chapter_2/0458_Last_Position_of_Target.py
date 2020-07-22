class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def lastPosition(self, nums, target):
        # write your code here
        if not nums:
            return -1
        
        left, right = 0, len(nums) - 1
        
            
        while left + 1 < right:
            if nums[right] == target:
                return right
            if nums[left] > target or nums[right] < target:
                return -1
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid
                continue
            if nums[mid] <= target:
                left = mid
                
        return left if nums[left] == target else -1
