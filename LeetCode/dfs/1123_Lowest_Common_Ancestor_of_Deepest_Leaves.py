# https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/discuss/334577/JavaC%2B%2BPython-Two-Recursive-Solution
# from this, you can also learn calculate tree height and find out the leaves

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # return tree height (bottom is 1) and lca
        def helper(root):
            if not root:
                return 0, None
            # height from bottom to top, leave is 1
            h_left, lca_left = helper(root.left)
            h_right, lca_right = helper(root.right)
            if h_left > h_right:
                # leaves in left side
                return h_left + 1, lca_left
            if h_right > h_left:
                return h_right + 1, lca_right
            # h_left == h_right, both sides have leaves
            return h_left + 1, root
        return helper(root)[1]
        
