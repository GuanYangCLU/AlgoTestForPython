"""
Definition of SegmentTreeNode:
class SegmentTreeNode:
    def __init__(self, start, end, max):
        self.start, self.end, self.max = start, end, max
        self.left, self.right = None, None
"""

class Solution:
    """
    @param A: a list of integer
    @return: The root of Segment Tree
    """
    def build(self, A):
        # write your code here
        return self._build(0, len(A) - 1, A)

    def _build(self, start, end, A):
        if start > end:
            return None
        node = SegmentTreeNode(start, end, A[start])
        if start == end:
            return node
        mid = (start + end) // 2
        node.left = self._build(start, mid, A)
        node.right = self._build(mid + 1, end, A)
        if node.left is not None and node.left.max > node.max:
            node.max = node.left.max
        if node.right is not None and node.right.max > node.max:
            node.max = node.right.max
        return node
      
