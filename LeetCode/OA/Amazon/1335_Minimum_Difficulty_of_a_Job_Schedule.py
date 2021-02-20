# TODO: DFS or n * d array update by whole column
# https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/discuss/924611/DFS-greater-DP-Progression-with-Explanation-O(n3d)O(nd)
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        # first j range: if contains i days slices
        jd = jobDifficulty
        if d > len(jd):
            # include jobDifficulty Empty due to d > 0
            return -1
        length = len(jd)
        dp = [[0] * length for row in range(2)]
        maxOfJobDf = jd[0]
        for j in range(length):
            maxOfJobDf = max(maxOfJobDf, jd[j])
            dp[1][j] = maxOfJobDf
        for i in range(2, d + 1):
            for j in range(length):
                if j + 1 < i:
                    dp[i % 2][j] = float('inf')
                    continue
                if j + 1 == i:
                    dp[i % 2][j] = dp[(i - 1) % 2][j - 1] + jd[j]
                    continue
                # need compare all possiblity after number i elements? any optimize?
                competitors = [dp[(i - 1) % 2][i + n - 2] + max(jd[i + n - 1:j + 1]) for n in range(j - i + 1)] + [dp[(i - 1) % 2][j - 1] + jd[j]]
                dp[i % 2][j] = min(competitors)
                # print(competitors, '|')
                # dp[i % 2][j] = min(dp[(i - 1) % 2][j - 2] + max(jd[j - 1], jd[j]), dp[(i - 1) % 2][j - 1] + jd[j])
                # if j == length - 1:
                #     print(dp[i % 2])
        # print(dp)
        return dp[d % 2][-1]
        
