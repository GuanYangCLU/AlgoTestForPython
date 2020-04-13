# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        self.helper(root, res)
        return res
        
    def helper(self, node, resArr):
        if not node:
            return
        resArr.append(node.val)
        self.helper(node.left, resArr)
        self.helper(node.right, resArr)
        
