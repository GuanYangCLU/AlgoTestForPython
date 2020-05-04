# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res, level = [], [root]
        while level and root:
            res.append([node.val for node in level])
            level = [child for childPair in level for child in (childPair.left, childPair.right) if child]
        return res
        
