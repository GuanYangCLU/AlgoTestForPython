"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def flatten(self, root):
        # write your code here
        self.flatten_and_return_last_node(root)
        
    def flatten_and_return_last_node(self, node):
        if not node:
            return None
            
        left_last = self.flatten_and_return_last_node(node.left)
        right_last = self.flatten_and_return_last_node(node.right)
        
        if left_last:
            left_last.right = node.right
            node.right = node.left
            node.left = None
            
        return right_last or left_last or node
