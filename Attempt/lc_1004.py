class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        if not A:
            return 0
        # (maxLen, curLen, index for len([j, i]) - sum([j, i]) <= k, sum)
        dp = [[0, 0, 0] for i in range(len(A))]
        maxLen = A[0]
        curLen = A[0]
        dp[0] = [maxLen, curLen, 0]
        memo = { (0,1): sum(A[0:1]) }
        for i in range(1, len(A)):
            
            lastValidIndex = dp[i-1][2]

            # print(lastValidIndex, i, A[lastValidIndex:i], len(A[lastValidIndex:i]) - sum(A[lastValidIndex:i]))
            lenFromTo = i - lastValidIndex
            memoSum = memo[(lastValidIndex, i)] if (lastValidIndex, i) in memo else sum(A[lastValidIndex:i])
            # print(lastValidIndex, i, A[lastValidIndex:i], lenFromTo, memoSum)
            
            # if (len(A[lastValidIndex:i]) - sum(A[lastValidIndex:i]) < K):
            if (lenFromTo - memoSum < K):
                
                dp[i][2] = dp[i-1][2]
            # elif (len(A[lastValidIndex:i]) - sum(A[lastValidIndex:i]) == K) and A[i] == 1:
            elif (lenFromTo - memoSum == K) and A[i] == 1:
                dp[i][2] = dp[i-1][2]
                
            else:
                dp[i][2] = dp[i-1][2] + 1
                
            dp[i][1] = i - dp[i][2] + A[i]
            dp[i][0] = max(dp[i - 1][0], dp[i][1])
        # print(dp)
        return dp[i][0]
