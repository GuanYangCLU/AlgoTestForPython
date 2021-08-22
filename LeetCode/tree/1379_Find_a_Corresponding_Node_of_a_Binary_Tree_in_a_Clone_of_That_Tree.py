# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        self.path = []
        self.getPath(original, target, [])
        return self.findNode(cloned, self.path)
    
    def getPath(self, node, target, path):
        if not node:
            return
        if node == target:
            self.path = path
            return
        self.getPath(node.left, target, path + ['left'])
        self.getPath(node.right, target, path + ['right'])
        
    def findNode(self, node, path):
        while path:
            side = path.pop(0)
            node = node.left if side == 'left' else node.right
        return node
        
