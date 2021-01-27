# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# maybe can optimize

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pLaNodes = self.dfs(root, p, [root])
        qLaNodes = self.dfs(root, q, [root])
        caNodes = [node for node in pLaNodes if node in qLaNodes]
        return caNodes[-1]
        
    def dfs(self, root, targetNode, laNodes):
        if not root:
            return
        
        # lcaNode = lcaNode if root.val > lcaNode.val else root
        laNodes.append(root)
        
        if root.val == targetNode.val:
            return laNodes
        
        leftLaNodes = self.dfs(root.left, targetNode, list(laNodes))
        rightLaNodes = self.dfs(root.right, targetNode, list(laNodes))
        return leftLaNodes if leftLaNodes else rightLaNodes
        
