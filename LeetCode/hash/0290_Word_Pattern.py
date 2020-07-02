class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        lst = str.split(' ')
        dic = {}
        if len(lst) != len(pattern):
            return False
        for i in range(len(pattern)):
            if pattern[i] in dic:
                if dic[pattern[i]] != lst[i]:
                    return False
            elif lst[i] in dic.values():
                return False
            else:
                dic[pattern[i]] = lst[i]
        return True
        
