# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head
        dummy, reverse = ListNode(0), None
        dummy.next = head
        pre = dummy
        for i in range(m - 1):
            pre = pre.next
        cur = pre.next
        for j in range(n - m + 1):
            next = cur.next
            cur.next = reverse
            reverse = cur
            cur = next
        pre.next.next = cur # 1 -> 2 <- 3 <- 4 ... 5, link 2 to 5
        pre.next = reverse # reverse is 4
        return dummy.next      
        
#         while idx <= n:
#             print(head.val)
#             if idx == m:
#                 tmp = head.next
#                 head.next = self.reverseTill(tmp, n - m, True, False)
#                 break
#             else:
#                 idx += 1
#                 head = head.next
#         return dummy.next
    
#     def reverseTill(self, head, l, isFirst, checked):
#         if l < 1:
#             temp = head.next
#             return head
#         elif head.next:
#             l -= 1
#             self.reverseTill(head, l, isFirst, checked).next = head
#             if isFirst:
#                 isFirst = False
#                 checked = True
#             return head
#         elif checked:
#             head.next = temp
#             return None
