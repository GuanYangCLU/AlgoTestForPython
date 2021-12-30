# Definition for a binary tree node.
# class TreeNode:
# https://www.jiuzhang.com/problem/recover-binary-search-tree/
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.firstEle = None
        self.secondEle = None
        self.lastEle = TreeNode(-float('inf'))
        
        self.dfs(root)
        # print(self.firstEle.val, self.secondEle.val)
        self.firstEle.val, self.secondEle.val = self.secondEle.val, self.firstEle.val
        # print(self.firstEle.val, self.secondEle.val)
        
    def dfs(self, node):
        if not node:
            return
        self.dfs(node.left)
        if not self.firstEle and node.val < self.lastEle.val:
            # now last ele stores value comparing with first val, in BST should find a desc case
            # still searching first one, left ele should lt last ele (wrong one)
            self.firstEle = self.lastEle
        if not (self.firstEle is None) and node.val < self.lastEle.val:
            # now last ele becomes storing value comparing second val
            # found first, then second should lt last ele (wrong one)
            self.secondEle = node
        # keep down and search
        self.lastEle = node
        
        self.dfs(node.right)
            
