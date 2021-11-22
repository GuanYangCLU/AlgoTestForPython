# https://leetcode.com/problems/find-and-replace-in-string/discuss/130587/C%2B%2BJavaPython-Replace-S-from-right-to-left

class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        # replace index from tail to head because after replace the S might change from i to end
        # but current i to start str won't change
        for i, s, t in sorted(zip(indexes, sources, targets), reverse=True):
            # if s matches slice in S, do replace, else stay same
            S = S[:i] + t + S[i + len(s):] if S[i:i + len(s)] == s else S
        return S
