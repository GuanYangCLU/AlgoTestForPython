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
        
