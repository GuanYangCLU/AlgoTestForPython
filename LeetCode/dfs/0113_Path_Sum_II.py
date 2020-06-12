# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []
        def helper(node, sum, path, res):
            if not node:
                return
            elif not node.left and not node.right:
                path = path[:] + [node.val]
                if node.val == sum:
                    res.append(path)
            else:
                path = path[:] + [node.val]
                helper(node.left, sum - node.val, path, res)
                helper(node.right, sum - node.val, path, res)    
        helper(root, sum, [], res)
        return res
