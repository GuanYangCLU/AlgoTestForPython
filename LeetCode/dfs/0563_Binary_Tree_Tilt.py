# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        def getSum(node):
            if not node:
                return 0
            return node.val + getSum(node.left) + getSum(node.right)
        def getMergedTilt(node):
            if not node:
                return 0
            return abs(getSum(node.left) - getSum(node.right)) + getMergedTilt(node.left) + getMergedTilt(node.right)
        
        if not root:
            return 0
        return getMergedTilt(root)
        
