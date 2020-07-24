class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def findPosition(self, nums, target):
        # write your code here
        if not nums:
            return -1
        
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right)  // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid - 1
                continue
            if nums[mid] < target:
                left = mid + 1

        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        return -1
