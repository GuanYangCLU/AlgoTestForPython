class Solution:
    """
    @param nums: a mountain sequence which increase firstly and then decrease
    @return: then mountain top
    """
    def mountainSequence(self, nums):
        # write your code here
        if not nums:
            return
        
        A = [-float('inf')] + nums + [-float('inf')]
        left, right, breakPoint = 1, len(nums), -1
            
        while left + 1 < right:
            mid = (left + right) // 2
            if A[left - 1] < A[left] and A[left] > A[left + 1]:
                return A[left]
            if A[right] > A[right - 1] and A[right] > A[right + 1]:
                return A[right]
            if A[mid] > A[mid - 1] and A[mid] > A[mid + 1]:
                return A[mid]
            if A[mid - 1] < A[mid] and A[mid] < A[mid + 1]:
                left = mid + 1
                continue
            if A[mid - 1] > A[mid] and A[mid] > A[mid + 1]:
                right = mid - 1
        
        return A[left]
