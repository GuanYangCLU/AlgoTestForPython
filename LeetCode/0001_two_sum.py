class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        dic = {}
        for i, n in enumerate(nums):
            if (n in dic):
                return [dic[n], i]
            dic[target - n] = i

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        dict = {i: (target - nums[i]) for i in range(len(nums))}
        for i in range(len(nums)):
            if (dict[i] in nums):#can only use once
                if (nums.index(dict[i]) != i):
                    return sorted([i,nums.index(dict[i])])          

nums = [3,3,4,1,2]
target = 6
p = Solution()
print(p.twoSum(nums,target))
        
"""
https://leetcode.com/problems/two-sum/submissions/
讨论区 动态判断

if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i

                
js的
const twoSum = (nums, target) => {
    const mapNums = new Map();
    for (let index = 0; index < nums.length; index++) {
        const indexFromMap = mapNums.get(nums[index]);
        if(indexFromMap != undefined) return [indexFromMap, index];
        mapNums.set(target - nums[index], index);    
    }
};                
"""            
