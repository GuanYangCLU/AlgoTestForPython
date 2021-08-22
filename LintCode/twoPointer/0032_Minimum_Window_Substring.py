class Solution:
    """
    @param source : A string
    @param target: A string
    @return: A string denote the minimum window, return "" if there is no such a string
    """
    def minWindow(self, source , target):
        # write your code here
        s = source
        t = target
        if not s or not t:
            return ''
        targetHash = self.getTargetHash(t)
        sourceHash = {}
        maxMatchedChars = len(targetHash)
        uniqueMatchedChars = 0
        s_len = len(s)
        # for update res trigger in loop phase 2
        minMatchedStrLength = s_len + 1
        res = ''
        j = 0
        
        for i in range(s_len):
            # phase 1: window rihgt side expand, s[j] will get in
            while j < s_len and uniqueMatchedChars < maxMatchedChars:
                if s[j] in targetHash:
                    # no need to car hash of char not in target
                    sourceHash[s[j]] = sourceHash.get(s[j], 0) + 1
                    if sourceHash[s[j]] == targetHash[s[j]]:
                        uniqueMatchedChars += 1
                j += 1
            # phase 2: till above procedure, all chars matched nums, and j is actually j + 1
            if j - i < minMatchedStrLength and uniqueMatchedChars == maxMatchedChars:
                minMatchedStrLength = j - i
                res = s[i:j]
            # phase 3: stop right side expand, start left side forward, s[i] will get out
            if s[i] in targetHash:
                if sourceHash[s[i]] == targetHash[s[i]]:
                    uniqueMatchedChars -= 1
                sourceHash[s[i]] -= 1
        return res
    
    def getTargetHash(self, target):
        targetHash = {}
        for c in target:
            targetHash[c] = targetHash.get(c, 0) + 1
        return targetHash
        
