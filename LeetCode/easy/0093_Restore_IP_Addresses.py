class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def isValid(ip):
            if len(ip) > 1 and ip[0] == '0':
                return False
            return int(ip) >= 0 and int(ip) < 256 
        l = len(s)
        res = []
        if l < 4 or l > 12:
            return []
        for i in range(1, 4):
            for k in range(l-1, l-4, -1):
                mid = s[i:k]
                midL = len(mid)
                if midL > 1 and midL < 7:
                    for j in range(i + 1, i + midL):
                        if isValid(s[:i]) and isValid(s[i:j]) and isValid(s[j:k]) and isValid(s[k:]):
                            res.append(('.').join([s[:i], s[i:j], s[j:k], s[k:]]))
        return res
