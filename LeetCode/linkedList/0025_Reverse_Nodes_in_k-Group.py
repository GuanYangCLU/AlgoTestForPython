# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # as max length is 5000, should valid for recursion, link to a asuumed reversed tail
        # length check
        if not head:
            return None
        checkIndexPointer = head
        for i in range(k):
            if not checkIndexPointer:
                # length < k
                return head
            checkIndexPointer = checkIndexPointer.next
        # length >= k
        head, tail = self.reverseAll(head, k)
        tail.next = self.reverseKGroup(checkIndexPointer, k)
        return head
    
    def reverseAll(self, head, k):
        if not head:
            return (None, None)
        if k == 1:
            return (head, head)
        newHead, newTail = self.reverseAll(head.next, k - 1)
        head.next = None
        newTail.next = head
        return (newHead, head)
        
