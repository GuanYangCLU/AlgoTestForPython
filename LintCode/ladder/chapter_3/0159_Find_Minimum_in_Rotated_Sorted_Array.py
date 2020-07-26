class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        # write your code here
        if not nums:
            return
        
        left, right = 0, len(nums) - 1
        minIdx = 0
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            if abs(nums[mid] - nums[left]) > abs(nums[mid] - nums[right]):
                right = mid
                continue
            if abs(nums[mid] - nums[left]) < abs(nums[mid] - nums[right]):
                left = mid
        
        if nums[left - 1] > nums[left]:
            return nums[left]
        return nums[right]
