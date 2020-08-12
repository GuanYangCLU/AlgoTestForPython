class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, candidates, target):
        # write your code here
        if not candidates:
            return []
        candidates.sort(reverse=True)
        res = set()
        self.dfs(candidates, target, [], res)
        return [list(comb) for comb in list(res)]
        
    def dfs(self, candidates, target, comb, res):
        if not candidates or target < 0:
            return
        for i in range(len(candidates)):
            if candidates[i] == target:
                res.add(tuple(sorted(comb + [candidates[i]])))
                continue
            self.dfs(candidates[i:], target - candidates[i], comb + [candidates[i]], res)
            
