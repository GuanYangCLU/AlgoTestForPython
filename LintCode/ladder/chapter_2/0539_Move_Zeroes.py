class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """
    def moveZeroes(self, nums):
        # write your code here
        if not nums:
            return []
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == 0:
                nums.append(nums.pop(i))
        return nums
