class Solution:
    """
    @param digits: A digital string
    @return: all posible letter combinations
    """
    def letterCombinations(self, digits):
        # write your code here
        if not digits:
            return []
        dict = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        res = set()
        self.dfs(digits, 0, dict, '', res)
        return list(res)
        
    def dfs(self, digits, index, dict, comb, res):
        if index == len(digits):
            res.add(comb)
            return
        for c in dict[digits[index]]:
            self.dfs(digits, index + 1, dict, comb + c, res)
