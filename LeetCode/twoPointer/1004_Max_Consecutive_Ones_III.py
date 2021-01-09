class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        if not A:
            return 0
        
        start, end = 0, 0
        # if first is 0 cost 1, k -> k-1
        currentK = K - (1 - A[end])
        currentMaxLen = A[start]
        while start < len(A) - 1 and end < len(A) - 1:
            # print(start, end, currentK, currentMaxLen)
            # right side move rule
            if currentK > 0 or currentK == 0 and A[end + 1] == 1:
                end += 1
                currentMaxLen = max(end - start + 1, currentMaxLen)
                currentK -= (1 - A[end])
                continue
            # left side move rule
            if currentK < 0 or currentK == 0 and A[end + 1] == 0:
                while A[start] == 1 and start <= end:
                    start += 1
                start += 1
                currentK += 1
        return currentMaxLen
                
    
# [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
# 3
# [1,1,1,0,0,0,1,1,1,1,0]
# 2
# [0,0,0,1]
# 4
# [0,0,0,0]
# 0
