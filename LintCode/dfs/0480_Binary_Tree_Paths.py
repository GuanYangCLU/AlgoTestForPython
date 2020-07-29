"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    def binaryTreePaths(self, root):
        # write your code here
        if not root:
            return []
            
        res = []
        self.findPath(root, [root], res)
        return res
        
    def findPath(self, node, path, res):
        if not node:
            return
        if not node.left and not node.right:
            res.append('->'.join([str(node.val) for node in path]))
            return
        if node.left:
            path.append(node.left)
            self.findPath(node.left, path, res)
            path.pop()
        if node.right:
            path.append(node.right)
            self.findPath(node.right, path, res)
            path.pop()
