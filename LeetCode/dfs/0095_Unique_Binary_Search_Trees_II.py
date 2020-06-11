# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        # use tree definition to construct tree recursively
        if n < 1:
            return []
        def treeDef(first, last):
            return [TreeNode(val, left, right)
                    for val in range(first, last + 1)
                    for left in treeDef(first, val - 1)
                    for right in treeDef(val + 1, last)] or [None] # edge case, do not forget
        return treeDef(1, n)
