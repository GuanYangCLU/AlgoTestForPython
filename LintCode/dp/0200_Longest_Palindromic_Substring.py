class Solution:
    """
    @param s: input string
    @return: a string as the longest palindromic substring
    """
    def longestPalindrome(self, s):
        # write your code here
        if not s:
            return ''
            
        length = len(s)
        start, res = 0, 1
        is_palindrome = [ [False] * length for _ in range(length) ]
        
        for i in range(length):
            is_palindrome[i][i] = True
        for i in range(1, length):
            is_palindrome[i][i - 1] = True
            
        for strLen in range(2, length + 1):
            for left in range(length - strLen + 1):
                right = left + strLen - 1
                is_palindrome[left][right] = is_palindrome[left + 1][right - 1] and s[left] == s[right]
                if is_palindrome[left][right] and strLen > res:
                    start, res = left, strLen

        return s[start:start + res]
