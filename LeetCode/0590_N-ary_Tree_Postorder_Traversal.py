"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        res = []
        def helper(node, res):
            for children in node.children:
                if not children.children:
                    res.append(children.val)
                else:
                    helper(children, res)
            res.append(node.val)
        helper(root, res)
        return res
        
