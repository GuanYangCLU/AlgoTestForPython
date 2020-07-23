class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):
        # write your code here
        # QUICKSORT, NEED REWRITE using different method like counting sort
        if not colors:
            return []
        
        left, right = 0, len(colors) - 1
        self.quickSort(0, len(colors) - 1, colors)
        
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
