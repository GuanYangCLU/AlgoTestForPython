class Solution:
    """
    @param A: sorted integer array A
    @param B: sorted integer array B
    @return: A new sorted integer array
    """
    def mergeSortedArray(self, A, B):
        # write your code here
        pointerA, pointerB = 0, 0
        res = []
        while pointerA < len(A) and pointerB < len(B):
            if A[pointerA] < B[pointerB]:
                res.append(A[pointerA])
                pointerA += 1
            else:
                res.append(B[pointerB])
                pointerB += 1
        else:
            if pointerA < len(A):
                return res + A[pointerA:]
            if pointerB < len(B):
                return res + B[pointerB:]
