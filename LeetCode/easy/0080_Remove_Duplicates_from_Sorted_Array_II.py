class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        originLen = len(nums)
        if originLen < 3:
            return originLen
        l, flag = 1, False
        for i in range(1, originLen):
            if nums[i] == nums[i-1]:
                if not flag:
                    flag = True
                    l += 1
                else:
                    nums.insert(0, nums.pop(i))
            else:
                flag = False
                l += 1
        del nums[0:originLen - l]
        return l
              
