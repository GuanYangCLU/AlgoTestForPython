# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        self.dfs(root, False)
        return self.res
    
    def dfs(self, node, isLonely):
        if not node:
            return
        if isLonely:
            self.res.append(node.val)
        self.dfs(node.left, node.right is None)
        self.dfs(node.right, node.left is None)
        
