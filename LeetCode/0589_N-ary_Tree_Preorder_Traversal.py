"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        res = []
        def helper(parent, valArr):
            if parent:
                valArr.append(parent.val)
                for child in parent.children:
                    if child:
                        helper(child, valArr)
        helper(root, res)
        return res
