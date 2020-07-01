class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # recursive iso, every time remove one from 26 letters
        if len(s) < 2:
            return True
        # ord('a'): 97, chr(97): 'a'
        # restMap = [chr(n) for n in range(97, 123)]
        usedDic = {}
        
        for i in range(len(s)):
            if s[i] in usedDic:
                # already pop up before
                if usedDic[s[i]] != t[i]:
                    # map to diff key
                    return False
            elif t[i] in usedDic.values():
                # diff letters map to same char
                return False
            else:
                usedDic[s[i]] = t[i]
        return True
        
