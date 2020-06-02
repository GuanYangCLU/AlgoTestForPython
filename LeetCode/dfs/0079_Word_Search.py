class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if self.dfs(board, i, j, word):
                    return True
        return False
    def dfs(self, board, i, j, word):
        m, n = len(board), len(board[0])
        # try except also handle?
        if len(word) == 0:
            return True
        if not i in range(m) or not j in range(n) or board[i][j] != word[0]:
            return False
        tmp = board[i][j]
        board[i][j] = '#' # mark as used
        res = self.dfs(board, i-1, j, word[1:]) or self.dfs(board, i, j+1, word[1:]) or self.dfs(board, i+1, j, word[1:]) or self.dfs(board, i, j-1, word[1:])
        board[i][j] = tmp
        return res
        
