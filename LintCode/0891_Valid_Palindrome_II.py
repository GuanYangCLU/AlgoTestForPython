class Solution:
    """
    @param s: a string
    @return bool: whether you can make s a palindrome by deleting at most one character
    """
    def validPalindrome(self, s):
        # Write your code here
        if not s or len(s) < 3:
            return True
        left, right = self.findDif(0, len(s) - 1, s) # work till dif pop
        if left >= right:
            return True
        return self.isPal(left + 1, right, s) or self.isPal(left, right - 1, s)
    
    def findDif(self, left, right, s):
        while left < right:
            if s[left] != s[right]:
                break
            left += 1
            right -= 1
        return left, right
        
    def isPal(self, left, right, s):
        newLeft, newRight = self.findDif(left, right, s)
        return newLeft >= newRight
