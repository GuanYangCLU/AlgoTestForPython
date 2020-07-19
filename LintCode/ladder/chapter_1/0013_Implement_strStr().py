class Solution:
    """
    @param source: 
    @param target: 
    @return: return the index
    """
    def strStr(self, source, target):
        # Write your code here
        if not target:
            return 0
        if not source:
            return -1
            
        wordIndex = 0
        for i in range(len(source)):
            if self.isSubString(source, target, i):
                return i
        return -1
        
    def isSubString(self, source, target, curSourceIndex):
        endIndex = curSourceIndex + len(target) - 1
        if endIndex > len(source) - 1:
            return False
        for j in range(curSourceIndex, endIndex + 1):
            if source[j] != target[j - curSourceIndex]:
                return False
        return True
