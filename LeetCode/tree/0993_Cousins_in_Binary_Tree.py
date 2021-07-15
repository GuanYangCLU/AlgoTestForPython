# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        # depth, parent = 0, 0 # val 0 does not exist in tree nodes
        depthX, parentX = self.getNodeInfo(root, x, 0, 0)
        depthY, parentY = self.getNodeInfo(root, y, 0, 0)
        return depthX == depthY and parentX != parentY
    
    def getNodeInfo(self, node, val, depth, parent):
        if not node:
            return None
        if node.val != val:
            resLeft = self.getNodeInfo(node.left, val, depth + 1, node.val)
            resRight = self.getNodeInfo(node.right, val, depth + 1, node.val)
            return resLeft if resLeft else resRight
        return depth, parent
