class Solution:
    """
    @param s: a string
    @param k: an integer
    @return: the number of substrings there are that contain at least k distinct characters
    """
    def kDistinctCharacters(self, s, k):
        # Write your code here
        if not s:
            return 0
        res = 0
        possible = 0
        containedChars = {}
        start, end = 0, 0
        while start <= end and start <= len(s) - k and end <= len(s):
            if self.getSize(containedChars) >= k:
                # res += possible
                
                possible = len(s) - end + 1
                res += possible
                # print(start, end, 'else', possible, res, containedChars)
                containedChars[s[start]] = containedChars.get(s[start], 0) - 1
                start += 1
                continue
            
            if end < len(s):
                containedChars[s[end]] = containedChars.get(s[end], 0) + 1
            # end - 1 is the real end
            end += 1

        return res
        
    def getSize(self, dic):
        size = 0
        if not dic.values():
            return 0
        for v in dic.values():
            if v > 0:
                size += 1
        return size
        
