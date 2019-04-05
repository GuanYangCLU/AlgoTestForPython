class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        elif len(nums) < 3:
            return max(nums)
        pre_lst = [0,nums[0]] # this list store the max val before 2 of current pos and before 1 of cur pos
        for i in range(1, len(nums)):
            tmp = pre_lst[1]
            pre_lst[1] = max(pre_lst[0] + nums[i], pre_lst[1])
            pre_lst[0] = tmp
        return max(pre_lst)
        # return max(sum(nums[::2]), sum(nums[1::2]))