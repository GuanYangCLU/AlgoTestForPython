class Solution:
    """
    @param a: The A array
    @param b: The B array
    @param s: The S string
    @return: The answer
    """
    def stringReplace(self, a, b, s):
        # Write your code here
        if not s:
            return ''
        
        infoA = [(len(word), word, index) for index, word in enumerate(a)]
        res = ''
        head = 0
        while head < len(s):
            replace = (0, '', -1)
            for i in range(len(infoA)):
                if head + infoA[i][0] - 1 > len(s) - 1:
                    continue
                if s[head:head + infoA[i][0]] == infoA[i][1]:
                    replace = max(replace, infoA[i])
            
            if replace[2] == -1:
                res += s[head]
                head += 1
                continue
            
            res += b[replace[2]]
            head += replace[0]

        return res
