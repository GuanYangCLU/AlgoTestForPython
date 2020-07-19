class Solution:
    """
    @param str: A String
    @param left: a left offset
    @param right: a right offset
    @return: return a rotate string
    """
    def RotateString2(self, str, left, right):
        # write your code here
        if not str:
            return ''
        
        move = (left - right) % len(str)
        if move < 0:
            move = len(str) + move
        
        return (str + str)[move:move + len(str)]
