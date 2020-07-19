class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """
    def longestPalindrome(self, s):
        # write your code here
        if not s:
            return 0
        dic = {}
        res = 0
        hasOddCount = False
        for c in s:
            dic[c] = dic.get(c, 0) + 1
        for n in dic.values():
            if not hasOddCount and n % 2 == 1:
                hasOddCount = True
                res += 1
            res += (n // 2) * 2
        return res
