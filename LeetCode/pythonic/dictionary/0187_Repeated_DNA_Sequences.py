class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        dic = {}
        for i in range(len(s) - 9):
            dic[s[i:i+10]] = dic.get(s[i:i+10], 0) + 1
        return [key for (key, value) in dic.items() if value > 1]
        
        
