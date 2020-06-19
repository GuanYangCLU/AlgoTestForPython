class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [True] + [False] * len(s)
        for i in range(len(s)):
            for j in range(i, len(s)):
                if dp[i] and s[i:j+1] in wordDict:
                    dp[j+1] = True
        # print(dp)
        return dp[-1]
        # def helper(s, dic):
        #     comb = False
        #     if not s:
        #         comb = True
        #     for w in dic:
        #         if s.find(w) == 0:
        #             comb = comb or helper(s[len(w):], dic)
        #     return comb
        # return helper(s, wordDict)
