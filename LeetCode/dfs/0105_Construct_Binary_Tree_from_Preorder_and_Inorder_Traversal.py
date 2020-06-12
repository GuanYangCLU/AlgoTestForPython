# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # same, use definition of tree
        if inorder:
            rootVal = preorder.pop(0)
            rootIdx = inorder.index(rootVal)
            root = TreeNode(rootVal)
            root.left = self.buildTree(preorder, inorder[0:rootIdx])
            root.right = self.buildTree(preorder, inorder[rootIdx+1:])
            return root
            
