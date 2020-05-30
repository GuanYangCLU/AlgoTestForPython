class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k == 0:
            return [[]]
        return [pre + [i] for i in range(k, n+1) for pre in self.combine(i-1, k-1)]
    #### Time Exceed?
        # def helper(nums, k, cb, res):
        #     if k == 0:
        #         if not sorted(cb) in res:
        #             res.append(sorted(cb))
        #         return
        #     for c in nums:
        #         subNums, cb_cp = nums[:], cb[:]
        #         # print(subNums, cb_cp,k)
        #         cb_cp.append(c)
        #         subNums.remove(c)
        #         helper(subNums, k-1, cb_cp, res)
        # res = []
        # helper(list(range(1, n+1)), k, [], res)
        # return res
        
