class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers2(self, A):
        # write your code here
        if not A:
            return []
        
        left, right = 0, len(A) - 1
        self.quickSort(0, len(A) - 1, A)
        
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
