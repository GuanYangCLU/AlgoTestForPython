# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        leafList1, leafList2 = [], []
        self.getLeafList(root1, leafList1)
        self.getLeafList(root2, leafList2)
        if len(leafList1) != len(leafList2):
            return False
        res = True
        for x, y in zip(leafList1, leafList2):
            res = res and x == y
        return res
    
    def getLeafList(self, node, lst):
        if not node:
            return
        self.getLeafList(node.left, lst)
        if not node.left and not node.right:
            lst.append(node.val)
        self.getLeafList(node.right, lst)
        
