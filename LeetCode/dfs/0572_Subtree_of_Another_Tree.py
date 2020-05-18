# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def transfer(node):
            return ('^' + str(node.val) + '#' + transfer(node.left) + transfer(node.right) if node else '$')
        return transfer(t) in transfer(s)
        
