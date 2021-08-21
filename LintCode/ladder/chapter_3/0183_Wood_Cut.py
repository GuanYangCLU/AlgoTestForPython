class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """
    def woodCut(self, L, k):
        # write your code here
        # when k = 1, size cannot gt maxL
        if not L:
            return 0
        size = min(max(L), sum(L) // k)
        if size == 0:
            return 0
        
        left, right = 1, size
        while left + 1 < right:
            mid = (left + right) // 2
            if self.getKBySize(L, mid) < k:
                right = mid
                continue
            if self.getKBySize(L, mid) >= k:
                left = mid
        
        return right if self.getKBySize(L, right) >= k else left
        
    def getKBySize(self, L, size):
        return sum([n // size for n in L])
