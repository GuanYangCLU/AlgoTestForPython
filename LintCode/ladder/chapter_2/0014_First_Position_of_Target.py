class Solution:
    """
    @param nums: The integer array.
    @param target: Target to find.
    @return: The first position of target. Position starts from 0.
    """
    def binarySearch(self, nums, target):
        # write your code here
        if not nums:
            return -1
        
        left, right = 0, len(nums) - 1
        
            
        while left + 1 < right:
            if nums[left] == target:
                return left
            if nums[right] < target or nums[left] > target:
                return -1
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid
                continue
            if nums[mid] >= target:
                right = mid
                
        return right if nums[right] == target else -1
