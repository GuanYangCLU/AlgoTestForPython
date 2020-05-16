# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        # max is among left sub, right sub, and merged tree
        self.res = 0 # avoid errror: referenced before assignment
        def getMaxDepth(node):
            if not node:
                return 0
            depL, depR = getMaxDepth(node.left), getMaxDepth(node.right)
            self.res = max(self.res, depL + depR) # compare with prev max in subtree and most possible by merged tree
            return 1 + max(depL, depR)
        getMaxDepth(root)
        return self.res
    
