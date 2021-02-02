"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: a root of binary tree
    @return: return a integer
    """
    def diameterOfBinaryTree(self, root):
        # write your code here
        maxDistance = 0
        return self.maxDist(root, maxDistance)
        
        
        
    def maxDepth(self, node):
        if not node:
            # can return -1, then maxDist should be l + r + 2
            return 0
        return max(self.maxDepth(node.left) + 1, self.maxDepth(node.right) + 1)
        
    def maxDist(self, node, maxDistance):
        if not node:
            return 0
        return max(self.maxDepth(node.left) + self.maxDepth(node.right), maxDistance)
        
