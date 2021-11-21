# https://www.jiuzhang.com/problem/lowest-common-ancestor-ii/

"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        # pop up p and record path node, then pop up q and check in path if visited
        visited = set()
        while p.parent:
            visited.add(p)
            p = p.parent
        while q.parent:
            if q in visited:
                return q
            q = q.parent
        return q
