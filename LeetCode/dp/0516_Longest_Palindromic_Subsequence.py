class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if not s:
            return 0
        if len(s) < 2:
            # guarantee str length at least 2 for dp min size
            return len(s)
        
        res = 1
        dp = [[1] * len(s) for _ in range(len(s))]
        for i in range(1, len(s)):
            dp[i][i-1] = 0
            
        # dynamic substr index of start and end
        # can not use for left for right because the direction is not first update row then next line
        # update by 对角线 use str length to control
        for length in range(2, len(s) + 1):
            for left in range(len(s) - 1):
                right = left + length - 1
                if right >= len(s):
                    continue
                if s[left] == s[right]:
                    dp[left][right] = 2 + dp[left + 1][right - 1]
                    continue
                # the way to record state instead of recursion
                dp[left][right] = max(dp[left + 1][right], dp[left][right - 1])

        return dp[0][len(s) - 1]

    '''
    dp[i][j] = longest palindrome subsequence of s[i to j].
    If s[i] == s[j], dp[i][j] = 2 + dp[i+1][j - 1]
    Else, dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    
    
    [
        [1, 2, 3, 3, 4],
        [0, 1, 2, 2, 3],
        [1, 0, 1, 1, 3],
        [1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1]
    ]
    
    '''
