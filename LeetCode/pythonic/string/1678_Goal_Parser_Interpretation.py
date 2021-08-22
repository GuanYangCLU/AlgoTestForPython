class Solution:
    def interpret(self, command: str) -> str:
        dic = { '()': 'o', '(al)': 'al' }
        res = command
        for key in dic.keys():
            res = self.splitAndJoin(res, key, dic[key])
        return res
    def splitAndJoin(self, s, key, val):
        return val.join(s.split(key))
        
