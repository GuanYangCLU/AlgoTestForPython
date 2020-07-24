class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2 
    @return: nothing
    """
    def sortColors(self, nums):
        # write your code here
        if not nums:
            return []
        
        left, right = 0, len(nums) - 1
        self.quickSort(0, len(nums) - 1, nums)
        
    def quickSort(self, left, right, nums):
        if left >= right:
            return
        pivot = nums[left + (right - left) // 2]
        start, end = left, right
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        self.quickSort(start, right, nums)
        self.quickSort(left, end, nums)
