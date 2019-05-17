# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = tail = ListNode(0) # 伪头
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1 # 插尾
                l1 = l1.next # 去头
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next # 更新尾
        tail.next = l1 or l2 # 最终尾
        # if not l1:
        #     tail.next = l2
        # else:
        #     tail.next = l1
            
        return dummy.next # 去伪头
        
'''
# recursive
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next =self.mergeTwoLists(l1,l2.next)
            return l2
'''
