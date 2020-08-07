class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        # write your code here
        if not nums:
            return [[]]
        nums.sort()
        res = []
        self.dfs(nums, 0, [], res)
        return res
        
    def dfs(self, nums, start, subset, res):
        res.append(subset[:])
        for i in range(start, len(nums)):
            subset.append(nums[i])
            self.dfs(nums, i + 1, subset, res)
            subset.pop()
