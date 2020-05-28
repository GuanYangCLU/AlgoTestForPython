# https://leetcode.com/problems/unique-paths-ii/discuss/146073/Python-DP-beat-100-python-submissions

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = obstacleGrid[:]
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if i == 0 and j == 0:
                    dp[i][j] = 1 - dp[i][j]
                elif i == 0 and j > 0:
                    dp[i][j] = min(dp[i][j-1], 1 - dp[i][j])
                elif i > 0 and j == 0:
                    dp[i][j] = min(dp[i-1][j], 1 - dp[i][j])
                else:
                    dp[i][j] = (dp[i][j-1] + dp[i-1][j]) * (1 - dp[i][j])
        return dp[len(obstacleGrid) - 1][len(obstacleGrid[0]) - 1]
                    
