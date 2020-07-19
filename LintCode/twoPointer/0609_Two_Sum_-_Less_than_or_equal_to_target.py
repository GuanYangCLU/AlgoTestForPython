class Solution:
    """
    @param nums: an array of integer
    @param target: an integer
    @return: an integer
    """
    def twoSum5(self, nums, target):
        # write your code here
        if not nums or len(nums) < 2:
            return 0
            
        sortedNums = sorted(nums)
        left, right, count = 0, len(sortedNums) - 1, 0
        
        while left < right:
            if sortedNums[left] + sortedNums[right] > target:
                count += left
                right -= 1
                continue
            if sortedNums[left] + sortedNums[right] <= target:
                print(count, left, right)
                count += (left + 1)
                left += 1
        return count
