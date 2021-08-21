"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        # write your code here
        res = []
        self.dfs(root, res)
        return res

    def dfs(self, node, res):
        if not node:
            return
        res.append(node.val)
        self.dfs(node.left, res)
        self.dfs(node.right, res)
