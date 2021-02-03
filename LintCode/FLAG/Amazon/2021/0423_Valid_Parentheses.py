class Solution:
    """
    @param s: A string
    @return: whether the string is a valid parentheses
    """
    def isValidParentheses(self, s):
        # write your code here
        pushed = []
        pairs = { ')': '(', ']': '[', '}': '{' }
        for c in s:
            if not c in pairs:
                pushed.append(c)
                continue
            if not pushed or pairs[c] != pushed[-1]:
                return False
            pushed.pop()
        return not pushed
        
