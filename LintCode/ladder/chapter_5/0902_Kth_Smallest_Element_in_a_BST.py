"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """
    def kthSmallest(self, root, k):
        # write your code here
        if not root:
            return
        self.k = k
        self.res = root.val
        self.dfs(root)
        return self.res
        
    def dfs(self, node):
        if not node:
            return
        self.dfs(node.left)
        self.k -= 1
        if self.k == 0:
            self.res = node.val
            return
        self.dfs(node.right)
