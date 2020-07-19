class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """
    def isPalindrome(self, s):
        # write your code here
        if not s:
            return True
        
        left, right = 0, len(s) - 1
        while left < right:
            if self.shouldSkip(left, s):
                left += 1
                continue
            if self.shouldSkip(right, s):
                right -= 1
                continue
            if s[left].upper() != s[right].upper():
                return False
            left += 1
            right -= 1
            
        return True
        
    def shouldSkip(self, index, s):
        return (not s[index].isdigit()) and (not s[index].isalpha())
