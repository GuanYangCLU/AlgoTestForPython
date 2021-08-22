# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        self.dic = {}
        self.dfs(root, 0)
        deepest = max(self.dic.keys())
        return self.dic[deepest]
        
    def dfs(self, node, lv):
        if not node:
            return
        self.dfs(node.left, lv + 1)
        self.dfs(node.right, lv + 1)
        self.dic[lv] = self.dic.get(lv, 0) + node.val
        
