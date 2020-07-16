# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        num = ''
        if not head:
            return 0
        while head:
            num += str(head.val)
            head = head.next
        return int(num, 2)
