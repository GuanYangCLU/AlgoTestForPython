class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        res, used = { 'A': 0, 'B': 0 }, []
        lstS, lstG = list(secret), list(guess)
        same = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                res['A'] = res.get('A', 0) + 1
                lstS = [lstS[i]] + lstS[:i] + lstS[i+1:]
                lstG = [lstG[i]] + lstG[:i] + lstG[i+1:]
                same += 1
        s, g = ''.join(lstS[same:]), ''.join(lstG[same:])
        for i in range(len(s)): 
            if s[i] in g:
                idx = g.index(s[i])
                res['B'] = res.get('B', 0) + 1
                g = g[:idx] + g[idx+1:] or ''
        return str(res['A']) + 'A' + str(res['B']) + 'B'
        
