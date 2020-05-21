class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curMaxReach = 0
        for i, n in enumerate(nums):
            if i > curMaxReach: # this position you cannot reach even you try best
                return False
            curMaxReach = max(curMaxReach, i+n) # update maxium reach
        return True # reach last index
        
