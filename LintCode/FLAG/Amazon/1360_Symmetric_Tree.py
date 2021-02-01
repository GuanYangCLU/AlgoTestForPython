"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

# observe and find abstract rules: each level subLeft mirror subRight
class Solution:
    """
    @param root: root of the given tree
    @return: whether it is a mirror of itself 
    """
    def isSymmetric(self, root):
        # Write your code here
        if not root:
            return True
        return self.isMirror(root.left, root.right)

    def isMirror(self, node1, node2):
        if not node1 and not node2:
            return True
        elif not node1 or not node2:
            return False
        return node1.val == node2.val and self.isMirror(node1.left, node2.right) and self.isMirror(node1.right, node2.left)

# 多此一举
class Solution:
    """
    @param root: root of the given tree
    @return: whether it is a mirror of itself 
    """
    def isSymmetric(self, root):
        # Write your code here
        if not root:
            return True
        cloneRoot = TreeNode(root.val)
        self.clone(root, cloneRoot)
        mirroredCloneRoot = self.mirror(cloneRoot)
        return self.isEqual(root, mirroredCloneRoot)
        
        
    def mirror(self, node):
        if not node:
            return
        node.left, node.right = self.mirror(node.right), self.mirror(node.left)
        return node
        
    def clone(self, node, cloneNode):
        if not node:
            return
        cloneNode.left = TreeNode(node.left.val) if node.left else None
        cloneNode.right = TreeNode(node.right.val) if node.right else None
        self.clone(node.left, cloneNode.left)
        self.clone(node.right, cloneNode.right)
    
    def isEqual(self, node1, node2):
        if not node1 and not node2:
            return True
        elif not node1 or not node2:
            return False
        return node1.val == node2.val and self.isEqual(node1.left, node2.left) and self.isEqual(node1.right, node2.right)
        
