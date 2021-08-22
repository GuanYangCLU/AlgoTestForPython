class Solution:
    def removeVowels(self, s: str) -> str:
        res = ''
        for c in s:
            if c not in 'aeiou':
                res += c
        return res
        
