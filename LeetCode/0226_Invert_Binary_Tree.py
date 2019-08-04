# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        # print('before ', root.left.val, root.right.val)
        root.left, root.right = root.right, root.left 
        # print(root.left.val, root.right.val)
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
