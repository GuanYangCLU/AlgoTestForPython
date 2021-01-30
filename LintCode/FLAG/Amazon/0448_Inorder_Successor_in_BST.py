"""
Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


class Solution:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """
    def inorderSuccessor(self, root, p):
        # write your code here
        if not root:
            return None
        if root.val <= p.val:
            # must be in right sub tree 
            return self.inorderSuccessor(root.right, p)
        # root > p, maybe root or in left sub tree, search in left until leaf
        left = self.inorderSuccessor(root.left, p)
        if not left:
            return root
        return left
        
