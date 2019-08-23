class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        if not A:
            return []
        left = 0
        right = len(A) - 1
        while left < right:
            if A[left] % 2 == 1:
                if A[right] % 2 == 0:
                    A[left], A[right] = A[right], A[left]
                else:
                    right -= 1
            else:
                left += 1        
        return A
