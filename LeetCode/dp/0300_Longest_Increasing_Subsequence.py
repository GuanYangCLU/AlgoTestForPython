# https://www.jiuzhang.com/problem/longest-increasing-subsequence/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp stores the min value of the last num of LIS with length i
        dp = [float('inf')] * (len(nums) + 1)
        dp[0] = -float('inf')
        res = 0
        for n in nums:
            index = self.first_gte(dp, n)
            dp[index] = n
            res = max(res, index)
        return res
    
    # nums is dp list, not the input nums here
    def first_gte(self, nums, target):
        start, end = 0, len(nums)
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid
                continue
            if nums[mid] >= target:
                end = mid
        return start if nums[start] >= target else end

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # store: 2nd len with min last, 1st len
        l = len(nums)
        if l < 2:
            return l
        size = 0
        tails = [0] * l
        for n in nums:
            lo, hi = 0, size
            while lo != hi:
                m = (lo + hi) // 2
                if tails[m] < n:
                    lo = m + 1
                else:
                    hi = m
            tails[lo] = n
            size = max(lo+1, size)
        return size
        
