class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        return self.binSearch(nums, 0, len(nums) - 1)
        
    def binSearch(self, nums, left, right):
        mid = (right - left + 1) // 2 + left
        if mid == left:
            return mid
        if nums[mid] - nums[mid - 1] > 0:
            return self.binSearch(nums, mid, right)
        return self.binSearch(nums, left, mid - 1)
        
