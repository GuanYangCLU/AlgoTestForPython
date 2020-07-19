class Solution:
    """
    @param: source: A source string
    @param: target: A target string
    @return: An integer as index
    """
    def strStr2(self, source, target):
        # write your code here
        if not target:
            return 0 if target == '' else -1
        if not source or len(source) < len(target):
            return -1
        
        BASE = 1000000
        SEED = 31
        
        power = 1
        for _ in range(len(target)):
            power = (power * SEED) % BASE
            
        hashCode, hashTarget = self.getHash(source[0:len(target)], BASE, SEED), self.getHash(target, BASE, SEED)
        for i in range(len(source) - len(target) + 1):
            if i == 0 and source[i:i + len(target)] == target:
                return 0
            if i > 0:
                hashCode = (hashCode * SEED) % BASE + ord(source[i + len(target) - 1]) - (ord(source[i - 1]) * power) % BASE
            if hashCode == hashTarget and  source[i:i + len(target)] == target:
                return i
        return -1
            
    def getHash(self, s, BASE, SEED):
        if not s:
            return 0
            
        res = 0
        for i in range(len(s)):
            res = ((res * SEED) % BASE) + ord(s[i])
        return res
