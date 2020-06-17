class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.dfs(s, [], res)
        return res
    def dfs(self, s, comb, res):
        if not s:
            res.append(comb)
            return
        for i in range(1, len(s)+1):
            if self.isValid(s[:i]):
                self.dfs(s[i:], comb + [s[:i]], res)
    def isValid(self, s):
        return s == s[::-1]
        
