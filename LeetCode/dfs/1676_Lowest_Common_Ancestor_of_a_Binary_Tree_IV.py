# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iv/discuss/957784/Python-clean-recursive-solution-O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        # common solution template for all nodes LCA
        # must all nodes in tree
        if not root:
            return None
        if root in nodes:
            return root
        left = self.lowestCommonAncestor(root.left, nodes)
        right = self.lowestCommonAncestor(root.right, nodes)
        if left and right:
            return root
        return left or right
