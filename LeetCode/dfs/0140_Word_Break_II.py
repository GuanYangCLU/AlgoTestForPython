class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        memo = {}
        return self.dfs(s, wordDict, memo)
    
    def dfs(self, s, wordDict, memo):
        if not s:
            return []
        if s in memo:
            return memo[s]
        
        new_partition = []
        if s in wordDict:
            new_partition.append(s)
        
        
        for i in range(1, len(s)):
            prefix = s[:i]
            if prefix not in wordDict:
                continue
            partition = self.dfs(s[i:], wordDict, memo)
            for w in partition:
                new_partition.append(prefix + ' ' + w)
        memo[s] = new_partition
        return new_partition
