import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        # newS =  re.sub(r'[^\w\s]|\s+', '', s.lower())
        left, right = 0, len(s) - 1
        while right > left:
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -=1
                continue
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
      
