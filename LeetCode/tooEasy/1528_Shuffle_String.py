class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        if not s:
            return ''
        res = [''] * len(s)
        for i in range(len(s)):
            res[indices[i]] = s[i]
        return ''.join(res)
