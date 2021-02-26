# standard
"""
Definition of SegmentTreeNode:
class SegmentTreeNode:
    def __init__(self, start, end):
        this.start, this.end = start, end
        this.left, this.right = None, None
"""

class Solution:	
    # @param start, end: Denote an segment / interval
    # @return: The root of Segment Tree
    def build(self, start, end):
        if start > end:
            return None
        root = SegmentTreeNode(start, end)
        if start == end:
            return root
        root.left = self.build(start, (start + end) / 2)
        root.right = self.build((start + end) / 2 + 1, end)
        return root

# self work
class Solution:
    """
    @param: start: start value.
    @param: end: end value.
    @return: The root of Segment Tree.
    """
    def build(self, start, end):
        # write your code here
        if start > end:
            return None
        root = SegmentTreeNode(start, end)
        return self._build(start, end, root)
        
    def _build(self, start, end, node):
        if start == end:
            return SegmentTreeNode(start, end)
        mid = (start + end) // 2
        node.left = self._build(start, mid, SegmentTreeNode(start, mid))
        node.right = self._build(mid + 1, end, SegmentTreeNode(mid + 1, end))
        return node
        
