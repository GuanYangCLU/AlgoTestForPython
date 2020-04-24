class Solution:
    def longestPalindrome(self, s: str) -> int:
        if not s:
            return 0
        dic = {}
        for c in s:
            if c in dic.keys():
                dic[c] += 1
            else:
                dic[c] = 1
        # vals = list(dic.values()) if len(list(dic.values())) else [dic.values()]
        vals = list(dic.values())
        evens = list(filter(lambda x: x % 2 == 0, vals))
        odds = list(filter(lambda x: x % 2 == 1, vals))
        num1 = sum(odds) - len(odds) + (1 if len(odds) else 0)
        num2 = sum(evens)
        print(odds, evens, vals, num1, num2)
        return num1 + num2
        # hash = set()
        # for c in s:
        #     if c not in hash:
        #         hash.add(c)
        #     else:
        #         hash.remove(c)
        # # len(hash) is the number of the odd letters
        # return len(s) - len(hash) + 1 if len(hash) > 0 else len(s)
        
