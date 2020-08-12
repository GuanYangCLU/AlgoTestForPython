class Solution:
    """
    @param: A: an integer array
    @param: k: a postive integer <= length(A)
    @param: targer: an integer
    @return: A list of lists of integer
    """
    def kSumII(self, A, k, target):
        # write your code here
        if not A:
            return []
        A.sort(reverse = True)
        res = set()
        self.dfs(A, k, target, [], res)
        return [list(comb) for comb in list(res)]
        
    def dfs(self, A, k, target, comb, res):
        if not A or target < 0 or k <= 0:
            return
        for i in range(len(A)):
            if A[i] == target and k == 1:
                res.add(tuple(sorted(comb + [A[i]])))
                continue
            self.dfs(A[i + 1:], k - 1, target - A[i], comb + [A[i]], res)
            
