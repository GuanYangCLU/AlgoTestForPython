"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        cloneNodeMap = {}
        cur = head
        cloneCur = cloneHead = Node(cur.val)
        cloneNodeMap[head] = cloneHead
        while cur:
            cloneCur.random = cur.random
            cloneCur.next = Node(cur.next.val) if cur.next else None
            if cur.next:
                cloneNodeMap[cur.next] = cloneCur.next
            cloneCur = cloneCur.next
            cur = cur.next
        copyP = cloneHead
        while copyP:
            copyP.random = cloneNodeMap[copyP.random] if copyP.random else None
            copyP = copyP.next
        return cloneHead
      
