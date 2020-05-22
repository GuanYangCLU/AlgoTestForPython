# https://leetcode.com/problems/count-binary-substrings/discuss/108626/Python-intuitive-approaches-with-explanation-(3-liner)
# '00001111' => [4, 4] => min(4, 4) => 4
# '00110' => [2, 2, 1] => min(2, 2) + min(2, 1) => 3
# '10101' => [1, 1, 1, 1, 1] => 4

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        res = 0
        breakPointLens = []
        start = 0
        for i in range(1, len(s)):
            if (s[i] != s[i-1]): # break point
                breakPointLens.append(i - start)
                start = i
            if (i == len(s) - 1):
                breakPointLens.append(i + 1 - start)
        for left, right in zip(breakPointLens[:-1], breakPointLens[1:]):
            res += min(left, right)
        return res

# time exceed
# class Solution:
#     def countBinarySubstrings(self, s: str) -> int:
#         def status(subStr):
#             l = len(subStr)
#             if '0' * (l // 2) + '1' * (l // 2) == subStr or '1' * (l // 2) + '0' * (l // 2) == subStr:
#                 return 'true'
#             if len(list(filter(None, subStr.split('0')))) > 1 or len(list(filter(None, subStr.split('1')))) > 1:
#                 return 'false'
#             return 'pending'
#         res = 0
#         for i in range(len(s) - 1):
#             for j in range(i + 1, len(s), 2):
#                 if status(s[i:j+1]) == 'true':
#                     res += 1
#                     break
#                 elif status(s[i:j+1]) == 'false':
#                     break
#                 else:
#                     continue
#         return res
