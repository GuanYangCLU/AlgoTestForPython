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
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def closestValue(self, root, target):
        # write your code here
        if not root:
            return
        closet = root.val
        return self.dfs(root, target, closet)
        
    def dfs(self, root, target, closet):
        if not root:
            return closet
        closet = root.val if abs(target - root.val) < abs(target - closet) else closet
        if root.val == target:
            return root.val
        if root.val < target:
            return self.dfs(root.right, target, closet)
        if root.val > target:
            return self.dfs(root.left, target, closet)
