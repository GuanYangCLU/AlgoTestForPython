class Solution:
    """
    @param str: A string
    @return: all permutations
    """
    def stringPermutation2(self, str):
        # write your code here
        res = set()
        self.dfs(str, 0, '', res)
        return list(res)
        
    def dfs(self, restStr, index, comb, res):
        if not restStr:
            res.add(comb)
            return
        memo = set()
        for i in range(len(restStr)):
            if restStr[i] in memo:
                continue
            memo.add(restStr[i])
            self.dfs(restStr[:i] + restStr[i + 1:], index + 1, comb + restStr[i], res)
