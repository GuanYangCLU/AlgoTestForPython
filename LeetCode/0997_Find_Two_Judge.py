class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if N == 1 and not trust: return 1
        stack = []
        test_len = 0
        for i in range(len(trust)):
            if trust[i][1] not in stack:
                stack.append(trust[i][1])
        for i in range(len(trust)):
            if trust[i][0] in stack:
                stack.pop(stack.index(trust[i][0]))
        if not stack: return -1
        else:
            for i in range(len(stack)):
                for j in range(len(trust)):
                    if trust[j][1] == stack[i]:
                        test_len += 1
                if test_len == N-1: return stack[i]
            return -1
