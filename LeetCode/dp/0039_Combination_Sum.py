class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def helper(tar, idx, curComb):
            if tar < 0:
                return
            elif tar == 0:
                res.append(curComb)
                return
            else:
                for i in range(idx, len(candidates)):
                    helper(tar - candidates[i], i, curComb + [candidates[i]])
        helper(target, 0, [])
        return res
        
# DP solution link:
# https://leetcode.com/problems/combination-sum/discuss/16506/8-line-Python-solution-dynamic-programming-beats-86.77

# DFS Link:
# https://leetcode.com/problems/combination-sum/discuss/16510/Python-dfs-solution.
