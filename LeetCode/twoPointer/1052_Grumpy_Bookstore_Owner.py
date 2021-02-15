class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        # premade to arrays: expectation of each day Ex[], Enhanced customers number En[]
        if not customers or not grumpy:
            return 0
        enhanced = 0
        prevXsum = [0]
        for x in range(X):
            prevXsum[0] += (customers[x] if grumpy[x] else 0)

        for i in range(len(customers) - X + 1):
            enhanced = max(enhanced, self.getSumEnhanced(customers, grumpy, X, i, prevXsum))
        preSum = sum([cus * (1 -val) for cus, val in zip(customers, grumpy)])
        return preSum + enhanced
        
    def getSumEnhanced(self, customers, grumpy, X, i, prevXsum):
        if i > 0:
            left = (customers[i - 1] if grumpy[i - 1] else 0)
            right = (customers[i + X - 1] if grumpy[i + X - 1] else 0)
            prevXsum[0] = prevXsum[0] + right - left

        return prevXsum[0]
        
