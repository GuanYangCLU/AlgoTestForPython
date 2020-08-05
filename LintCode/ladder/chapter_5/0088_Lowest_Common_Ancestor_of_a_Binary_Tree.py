"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: A: A TreeNode in a Binary.
    @param: B: A TreeNode in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """
    def lowestCommonAncestor(self, root, A, B):
        # write your code here
        if not root:
            return
        return self.dfs(root, A, B)
        
    def dfs(self, node, A, B):
        if not node:
            return
        if node in [A, B]:
            return node
        left = self.dfs(node.left, A, B)
        right = self.dfs(node.right, A, B)
        if left and right:
            return node
        if left and not right:
            return left
        if right and not left:
            return right
