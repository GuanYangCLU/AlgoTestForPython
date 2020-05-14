# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        level = [root]
        while len(level) > 0:
            if len(res) % 2 == 0:
                res.append([node.val for node in level])
            else:
                res.append(list(reversed([node.val for node in level])))
            level = [child for node in level for child in (node.left, node.right) if child ] # same as JS map and filter
        return res
                
