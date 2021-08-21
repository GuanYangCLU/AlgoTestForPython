# 二分答案集，参考LintCode 183： Wood Cut
class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        if not ribbons:
            return 0
        size = min(max(ribbons), sum(ribbons) // k)
        if size == 0:
            return 0
        
        left, right = 1, size
        while left + 1 < right:
            mid = (left + right) // 2
            if self.getNumBySize(mid, ribbons) < k:
                right = mid
                continue
            if self.getNumBySize(mid, ribbons) >= k:
                left = mid
        # print(left, right, self.getNumBySize(left, ribbons), self.getNumBySize(right, ribbons), k)
        return right if self.getNumBySize(right, ribbons) >= k else left
    
    def getNumBySize(self, size, ribbons):
        return sum([l // size for l in ribbons])
