# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Classic linked list, need to practice

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # recite: getMid, reverse, edit element
        if not head:
            return
        # 1. get mid
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        cur = slow.next
        slow.next = None
        curReversedHead = None
        # 2. reverse, recursively assign a_n next to group of reversed a_n-1
        while cur:
            nextNode = cur.next # nextNode now store next ele
            cur.next = curReversedHead # construct n+1 reversed group with head cur
            curReversedHead = cur # move head from n-1 to n cur
            cur = nextNode # update cur always point to next ele
        # 3. insert node
        node = head
        while curReversedHead:
            tmp = curReversedHead.next
            curReversedHead.next = node.next
            node.next = curReversedHead
            node = node.next.next # move 2 steps
            curReversedHead = tmp
