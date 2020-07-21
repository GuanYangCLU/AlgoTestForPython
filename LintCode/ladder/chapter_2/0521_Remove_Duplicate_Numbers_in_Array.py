class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums):
        # write your code here
        if not nums:
            return 0
        
        dic = {}
        count = len(nums)
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] not in dic:
                dic[nums[i]] = True
                continue
            count -= 1
            nums[i] = nums[count]
            
        return count
