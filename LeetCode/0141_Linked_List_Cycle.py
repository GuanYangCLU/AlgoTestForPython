# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# can only use race, why last.next will return error?
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if not slow or not fast or not fast.next or not fast.next.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
        
