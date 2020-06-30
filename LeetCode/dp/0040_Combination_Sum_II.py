class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        res = []
        dic = {}
        def helper(tar, idx, comb):
            if tar < 0 or idx == len(candidates):
                return
            elif tar == 0:
                key = ','.join(str(sorted(comb)))
                if not key in dic:
                    res.append(comb)
                    dic[key] = True
                return
            else:
                for i in range(idx + 1, len(candidates)):
                    helper(tar - candidates[i], i, comb + [candidates[i]])
        helper(target, -1, [])
        return res
        
