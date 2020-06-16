"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # recursion cost extra space so use loop
        dummy = Node(0)
        dummy.next = root
        while root and root.left:
            # start from the first element of each row level by level
            head = root.left # next row's first element
            while root:
                # loop through finishing each row
                root.left.next = root.right
                root.right.next = root.next and root.next.left
                root = root.next
            root = head # jump to next row
        return dummy.next
        
