# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.res = 0
        self.dfs(root)
        return root
    def dfs(self, node):
        if not node:
            return
        self.dfs(node.right)
        self.res += node.val
        node.val = self.res
        self.dfs(node.left)
        
