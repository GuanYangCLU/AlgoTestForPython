class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        if not A:
            return []
        for i in range(len(A)):
            A[i] *= A[i]
        A.sort()
        return A
