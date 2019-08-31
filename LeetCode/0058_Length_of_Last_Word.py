class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        sl = s[::-1]
        for a in sl:
            if a != ' ': break
            else: sl = sl[1:]
        return sl.index(' ') if ' ' in sl else len(sl)
