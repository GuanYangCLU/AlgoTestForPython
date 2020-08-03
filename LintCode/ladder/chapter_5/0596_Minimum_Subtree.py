"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """
    def findSubtree(self, root):
        # write your code here
        if not root:
            return
        node, rootSum, minSum = self.dfs(root)
        return node
        
    def dfs(self, node):
        if not node:
            return (None, 0, float('inf'))
        (leftMinNode, leftSum, leftMinSum), (rightMinNode, rightSum, rightMinSum) = self.dfs(node.left), self.dfs(node.right)
        minSum = min(leftMinSum, rightMinSum, node.val + leftSum + rightSum)

        if minSum == node.val + leftSum + rightSum:
            return (node, minSum, minSum)
        if minSum == leftMinSum:
            return (leftMinNode, node.val + leftSum + rightSum, minSum)
        if minSum == rightMinSum:
            return (rightMinNode, node.val + leftSum + rightSum, minSum)
