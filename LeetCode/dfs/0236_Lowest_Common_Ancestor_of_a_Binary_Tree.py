# https://www.jiuzhang.com/problem/lowest-common-ancestor-of-a-binary-tree/
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/discuss/158060/Python-DFS-tm

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root == p or root == q:
            return root
        left_search_res = self.lowestCommonAncestor(root.left, p, q)
        right_search_res = self.lowestCommonAncestor(root.right, p, q)
        
        if left_search_res and right_search_res:
            return root
        # notice: return search_res, not the root.left
        # because the res might be decided in very low level and pop up top
        # should keep record the node in low level
        if left_search_res:
            return left_search_res
        if right_search_res:
            return right_search_res
        return None
