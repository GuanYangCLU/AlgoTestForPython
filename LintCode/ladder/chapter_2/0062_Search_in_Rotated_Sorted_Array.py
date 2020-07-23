class Solution:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """
    def search(self, A, target):
        # write your code here
        # firs BS find break point
        # second BS find target
        if not A:
            return -1
        
        left, right, breakPoint = 0, len(A) - 1, 0
        start, end = left, right
        if A[start] == target:
            return start
        if A[end] == target:
            return end
            
        while left + 1 < right:
            mid = (left + right) // 2
            if A[left - 1] > A[left]:
                breakPoint = left
                break
            if A[right] < A[right - 1]:
                breakPoint = right
                break
            if A[mid] < A[mid - 1]:
                breakPoint = mid
                break
            if A[mid] > A[mid + 1]:
                breakPoint = mid + 1
                break
            if abs(A[mid] - A[left]) > abs(A[mid] - A[right]):
                right = mid
                continue
            if abs(A[mid] - A[left]) < abs(A[mid] - A[right]):
                left = mid
                
        if A[breakPoint] == target:
            return breakPoint
        if A[breakPoint - 1] == target:
            return breakPoint - 1
        if A[start] < target < A[breakPoint - 1]:
            return self.binarySearch(start, breakPoint - 1, target, A)
        if A[end] > target > A[breakPoint]:
            return self.binarySearch(breakPoint, end, target, A)
        return -1
            
    def binarySearch(self, start, end, target, A):
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] == target:
                return mid
            if A[mid] > target:
                end = mid
                continue
            if A[mid] < target:
                start = mid
        return -1
