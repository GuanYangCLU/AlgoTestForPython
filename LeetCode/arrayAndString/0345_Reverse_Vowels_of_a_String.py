VOWELS = ['a', 'e', 'i', 'o', 'u']

class Solution:
    def reverseVowels(self, s: str) -> str:
        if not s:
            return s
        left, right = 0, len(s) - 1
        returnStr = s
        while right > left:
            if returnStr[left].lower() not in VOWELS:
                left += 1
                continue
            if returnStr[right].lower() not in VOWELS:
                right -= 1
                continue
            #L, R stop on vowels
            returnStr = self.swapInStr(returnStr, left, right)
            left += 1
            right -= 1
        return returnStr
    
    def swapInStr(self, s, left, right):
        return s[:left] + s[right] + s[left + 1 : right] + s[left] + s[right + 1:]
