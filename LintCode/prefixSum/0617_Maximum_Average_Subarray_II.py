class Solution:
    """
    @param nums: an array with positive and negative numbers
    @param k: an integer
    @return: the maximum average
    """
    def maxAverage(self, nums, k):
        # write your code here
        if not nums:
            return -float('\inf')
        
        n = len(nums)
        prefix_sum = [0]
        sum_num = 0.
        for i in range(n):
            sum_num += nums[i]
            prefix_sum.append(sum_num)
        
        # store max_avg in index i and its length
        dp = [(-float('inf'), 0)] * n
        # initiate [0, k-1]
        dp[k - 1] = max(dp[k - 1], (prefix_sum[k] / k, k))
        
        # if final result length > k, it must contain a certain part of k length basic range
        for end in range(k, n):
            avg = (prefix_sum[end + 1] - prefix_sum[end + 1 - k]) / k
            # get before max_avg and the length at that avg
            pre_max_avg, pre_length = dp[end - 1]
            # start from length k, every time add one val use this formula to calculate length + 1 value
            new_avg = (pre_max_avg * pre_length + nums[end]) / (pre_length + 1)
            dp[end] = max((new_avg, pre_length + 1), (avg, k))

        return max(dp)[0]
        
