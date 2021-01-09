class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        if not A:
            return 0
        # (maxLen, curLen, index for len([j, i]) - sum([j, i]) <= k, sum)
        dp = [[0, 0, 0] for i in range(len(A))]
        maxLen = A[0]
        curLen = A[0]
        dp[0] = [maxLen, curLen, 0]
        memo = { (0,1): sum(A[0:1]) }
        for i in range(1, len(A)):
            
            lastValidIndex = dp[i-1][2]

            # print(lastValidIndex, i, A[lastValidIndex:i], len(A[lastValidIndex:i]) - sum(A[lastValidIndex:i]))
            lenFromTo = i - lastValidIndex
            memoSum = memo[(lastValidIndex, i)] if (lastValidIndex, i) in memo else sum(A[lastValidIndex:i])
            # print(lastValidIndex, i, A[lastValidIndex:i], lenFromTo, memoSum)
            
            # if (len(A[lastValidIndex:i]) - sum(A[lastValidIndex:i]) < K):
            if (lenFromTo - memoSum < K):
                
                dp[i][2] = dp[i-1][2]
            # elif (len(A[lastValidIndex:i]) - sum(A[lastValidIndex:i]) == K) and A[i] == 1:
            elif (lenFromTo - memoSum == K) and A[i] == 1:
                dp[i][2] = dp[i-1][2]
                
            else:
                dp[i][2] = dp[i-1][2] + 1
                
            dp[i][1] = i - dp[i][2] + A[i]
            dp[i][0] = max(dp[i - 1][0], dp[i][1])
        # print(dp)
        return dp[i][0]
    
# class Solution:
#     def longestOnes(self, A: List[int], K: int) -> int:
#         if not A:
#             return 0
        
#         start, end = 0, 0
#         currentK = K
#         firstZeroIndex = 0
#         currentMaxLen = A[start]
#         hasFirstZero = False
#         while start < len(A) and end < len(A):
#             # print(start, end, firstZeroIndex, currentK, currentMaxLen, hasFirstZero)
#             if A[start] == 0:
#                 hasFirstZero = True
#                 firstZeroIndex = start

            
#             if A[end] == 0:
#                 if not hasFirstZero:
#                     firstZeroIndex = end
#                     hasFirstZero = True
#                 currentK -= 1
                
                        
#             if self.shouldCutOff(currentK, end, A):
#                 currentMaxLen = max(currentMaxLen, end - start)
#                 start = firstZeroIndex + 1
#                 end = firstZeroIndex + currentMaxLen
#                 print(start, end)
#                 if end >= len(A) - 1:
#                     break
#                 numOfZero = end - start + 1 - sum(A[start:end + 1]) - K
#                 print(numOfZero, currentMaxLen, end - start + 1, sum(A[start:end + 1]))
#                 while numOfZero > 0:
#                     start += 1
#                     end += 1
#                     if end >= len(A) - 1:
#                         break
#                     numOfZero = numOfZero - A[end] + A[start - 1]
                    
#                 currentK = K
#                 hasFirstZero = False
#                 continue
            
#             end += 1
#             if end >= len(A) - 1:
#                 currentMaxLen = max(currentMaxLen, len(A) - 1 - start)
                
#             # currentMaxLen += A[end] # actually weight of len
#         return currentMaxLen
            
#     def shouldCutOff(self, currentK, currentIndex, A):
#         # cut till valid list including and extra 0 at last: [...validList, 0]
#         # hitBoundaryInRange = currentIndex < len(A) - 1 and A[currentIndex + 1] == 0
#         # hitBoundaryAtEnd = currentIndex == len(A) - 1
#         return currentK < 0
#     #  and A[currentIndex] == 0
    
# [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
# 3
# [1,1,1,0,0,0,1,1,1,1,0]
# 2
# [0,0,0,1]
# 4
# [0,0,0,0]
# 0
