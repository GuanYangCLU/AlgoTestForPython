# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.calcu_h(root) != -1
    def calcu_h(self, root):
        if not root:
            return 0
        left = self.calcu_h(root.left)
        right = self.calcu_h(root.right)
        if left == -1 or right == -1:
            return -1
        if abs(left - right) > 1: 
            return -1
        return max(left, right) + 1 # first compare the max depth, then we can calcu +1

'''
https://leetcode.com/problems/balanced-binary-tree/discuss/157645/Python-Tree-tm
'''        
        
'''
失败待研究
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return Solution.calcu_max_h(root) <= 1
    def is_leaf(root):
        return root.left == None and root.right == None
    def calcu_h(root):
        if not root:
            return 0
    #     left = self.calcu_h(root.left)
    #     right = self.calcu_h(root.right)
    #     if left == -1 or right == -1:
    #         return -1
    #     if abs(left - right) > 1: 
    #         return -1
    #     return max(left, right) + 1 # first compare the max depth, then we can calcu +1
        elif root.left == None:
            return Solution.calcu_h(root.right)+1
        elif root.right == None:
            return Solution.calcu_h(root.left)+1
        else:
            return max(Solution.calcu_h(root.left), Solution.calcu_h(root.right))+1
    def calcu_max_h(root):
        if root == None:
            return 0
        elif root.left == None or root.right == None:
            return Solution.calcu_h(root)-1
        elif Solution.is_leaf(root.left) or Solution.is_leaf(root.right):
            return abs(Solution.calcu_h(root.left) - Solution.calcu_h(root.right))
        else:
            return max(Solution.calcu_max_h(root.left), Solution.calcu_max_h(root.right))+1
            # return abs(Solution.calcu_h(root.left) - Solution.calcu_h(root.right))
'''