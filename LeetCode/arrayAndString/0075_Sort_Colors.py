class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # dic = {
        #     '0': 0,
        #     '1': 0,
        #     '2': 0
        # }
        # for n in nums:
        #     dic[str(n)] += 1
        # nums = [0] * dic['0'] + [1] * dic['1'] + [2] * dic['2']
        # print(nums)
        # return nums
        
        # take turns to overwrite color
        r, w = 0, 0 # keep paint forward, blue as base, white overwrite blue and red overwrite white
        for b in range(len(nums)):
            val = nums[b]
            nums[b] = 2
            if val < 2:
                nums[w] = 1
                w += 1
            if val == 0:
                nums[r] = 0
                r += 1
                
