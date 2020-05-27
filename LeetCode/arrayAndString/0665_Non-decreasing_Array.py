class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return True
        planA, planB = nums[:], nums[:]
        for i in range(len(nums) - 1):
            # smooth zipper = [nums[i], nums[i+1]]
            if nums[i+1] < nums[i]:
                planA[i] = nums[i+1]
                planB[i+1] = nums[i]
                break
        return planA == sorted(planA) or planB == sorted(planB)
    
