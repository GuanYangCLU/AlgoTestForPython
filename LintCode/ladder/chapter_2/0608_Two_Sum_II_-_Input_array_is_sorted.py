class Solution:
    """
    @param nums: an array of Integer
    @param target: target = nums[index1] + nums[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, nums, target):
        # write your code here
        left, right = 1, len(nums)
        while left < right:
            sumVal = nums[left - 1] + nums[right - 1]
            if sumVal == target:
                return [left, right]
            if sumVal > target:
                right -= 1
                continue
            if sumVal < target:
                left += 1
                
