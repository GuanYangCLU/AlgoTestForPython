class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        rs = []
        if not A:
            return rs
        for i in range(1, len(A)):
            if len(A[i]) < len(A[i-1]):
                A[i], A[i-1] = A[i-1], A[i]
        if not A[0]:
            return rs
        for i in range(len(A[0])):
            count = 0
            for j in range(1, len(A)):
                if A[0][i] in A[j]:                  
                    count += 1
                else:
                    break
            if count == len(A) - 1:
                rs.append(A[0][i])
                for j in range(1, len(A)):
                    A[j] = A[j][:A[j].index(A[0][i])] + A[j][A[j].index(A[0][i])+1:]
        return rs
