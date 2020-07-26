class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def kClosestNumbers(self, A, target, k):
        # write your code here
        # get lst of len(k) asc order
        # 2 pointer partition
        if not A:
            return []
        if len(A) == k:
            return self.orderedRes(A, target)
            
        left, right = 0, len(A) - k
        
        while left + 1 < right:
            mid = (left + right) // 2
            if target - A[mid] > A[mid + k] - target:
                left = mid
                continue
            right = mid
            
        print(left, right)
        
        start = right if target - A[left] > A[left + k] - target else left
        tempRes = A[start:start + k]
        
        print(tempRes)
        
        return self.orderedRes(tempRes, target)
        
    def orderedRes(self, nums, target):
        if not nums:
            return []
        numsInfo = [(abs(n - target), n) for n in nums]
        return [x[1] for x in sorted(numsInfo)]
