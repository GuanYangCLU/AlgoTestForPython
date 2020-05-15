# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        res = []
        def search(node, path):
            if not node:
                return
            path = str(node.val) if not path else path + '->' + str(node.val)
            if not node.left and not node.right:
                res.append(path)
                return
            search(node.left, path)
            search(node.right, path)
        search(root, '')
        return res
        
