# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        return self.getOneSideCrossSidesMaxPathSum(root)[1]
        
    def getOneSideCrossSidesMaxPathSum(self, node):
        # return oneSideMax, realMax
        if not node:
            return 0, -float('inf')
        left = self.getOneSideCrossSidesMaxPathSum(node.left)
        right = self.getOneSideCrossSidesMaxPathSum(node.right)
        # must contain node or it cut off
        oneSide = max(
            node.val + left[0], 
            node.val + right[0],
            0
        )
        maxPath = max(
            left[1],
            right[1],
            left[0] + node.val + right[0]
        )
        return oneSide, maxPath
        
