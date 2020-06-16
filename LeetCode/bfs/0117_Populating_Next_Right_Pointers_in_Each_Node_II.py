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
        dummy = Node(0)
        dummy.next = root
        cur = head = Node(0)
        # head record the last element of last row, head.next shoould be pointed to first element
        while root:
            # check if left exists
            cur.next = root.left
            if cur.next:
                # continue
                cur = cur.next
            cur.next = root.right
            if cur.next:
                cur = cur.next
            # root.next was set in last row
            root = root.next
            if not root:
                cur = head
                root = head.next
        return dummy.next
        
