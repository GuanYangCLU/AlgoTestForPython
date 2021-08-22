class Solution:
    def sortSentence(self, s: str) -> str:
        sortedInput = sorted([self.getIndexAndValue(item) for item in s.split()])
        res = ' '.join([item[1] for item in sortedInput])
        return res
        
    def getIndexAndValue(self, item):
        index = int(item[-1])
        value = item[:len(item) - 1]
        return index, value
        
