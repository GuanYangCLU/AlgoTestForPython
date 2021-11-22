# https://leetcode.com/problems/longest-string-chain/discuss/294890/JavaC%2B%2BPython-DP-Solution

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = {}
        for w in sorted(words, key=len):
            # check if exists a word just miss one char compare with cur word
            # if so, find the max value which means the chain length
            dp[w] = max(dp.get(w[:i] + w[i+1:], 0) + 1 for i in range(len(w)))
        return max(dp.values())
      
