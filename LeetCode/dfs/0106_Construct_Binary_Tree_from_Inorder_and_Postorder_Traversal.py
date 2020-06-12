# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if inorder:
            rootVal = postorder.pop()
            rootIdx = inorder.index(rootVal)
            root = TreeNode(rootVal)
            root.right = self.buildTree(inorder[rootIdx+1:], postorder)      
            root.left = self.buildTree(inorder[0:rootIdx], postorder)
            return root
            
