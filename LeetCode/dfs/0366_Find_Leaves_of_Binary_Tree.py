# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = []
        self.entry = []

    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return self.res
        dummy = TreeNode(0, root)
        while dummy.left:
            self.dfs(root, dummy, 'left')
            self.res.append(list(self.entry))
            self.entry = []
        return self.res
    
    def dfs(self, node, parent, side):
        if not node:
            return
        if not node.left and not node.right:
            self.entry.append(node.val)
            if parent and side == 'left':
                parent.left = None
            if parent and side == 'right':
                parent.right = None
            return
        self.dfs(node.left, node, 'left')
        self.dfs(node.right, node, 'right')
        
