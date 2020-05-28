# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return
        l = 1
        node = temp = head
        while node.next:
            l += 1
            node = node.next
        node.next = head
        cutIdx = l - k % l
        index = 1
        while index < cutIdx:
            index += 1
            temp = temp.next
        res = temp.next
        temp.next = None
        return res
