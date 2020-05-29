class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        for itv in sorted(intervals, key = lambda itv: itv[0]):
            if res and res[-1][1] >= itv[0]:
                res[-1][1] = max(res[-1][1], itv[1])
            else:
                res.append(itv)
        return res
        
