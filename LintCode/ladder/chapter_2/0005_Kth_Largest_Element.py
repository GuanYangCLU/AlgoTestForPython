class Solution:
    """
    @param n: An integer
    @param nums: An array
    @return: the Kth largest element
    """
    def kthLargestElement(self, n, nums):
        # write your code here
        left, right = 0, len(nums) - 1
        return self.quickSort(0, len(nums) - 1, nums, n)
        
    def quickSort(self, left, right, nums, n):
        if left >= right:
            return nums[right]
        pivot = nums[left + (right - left) // 2]
        start, end = left, right
        while left <= right:
            while left <= right and nums[left] > pivot:
                left += 1
            while left <= right and nums[right] < pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        if right + 1  == n - 1:
            return pivot
        if right + 1 > n - 1:
            return self.quickSort(start, right, nums, n)
        if right + 1 < n - 1:
            return self.quickSort(left, end, nums, n)
