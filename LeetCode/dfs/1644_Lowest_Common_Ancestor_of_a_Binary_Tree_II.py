# https://www.jiuzhang.com/problem/lowest-common-ancestor-iii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # pattern mostly stays same, just add found_p and found_q check before LCA search
        # helper return found_p, found_q, lca
        def helper(root, p, q):
            if not root:
                return False, False, None
            left_found_p, left_found_q, left_lca = helper(root.left, p, q)
            right_found_p, right_found_q, right_lca = helper(root.right, p, q)
            
            found_p = left_found_p or right_found_p or root is p
            found_q = left_found_q or right_found_q or root is q
            # rest pattern won't change
            if root is p or root is q:
                return found_p, found_q, root
            if left_lca and right_lca:
                return found_p, found_q, root
            if left_lca:
                return found_p, found_q, left_lca
            if right_lca:
                return found_p, found_q, right_lca
            return found_p, found_q, None
        found_p, found_q, lca = helper(root, p, q)
        return lca if found_p and found_q else None
            
