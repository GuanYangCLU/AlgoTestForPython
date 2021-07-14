# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        if not head.next:
            return head
        listRefs = []
        cur = head
        while cur:
            listRefs.append(cur)
            cur = cur.next
        # if k == 1 or k == len(listRefs):
        #     listRefs[-1].next = listRefs[1]
        #     listRefs[-2].next = listRefs[0]
        #     listRefs[0].next = None
        #     return listRefs[-1]
        # if k == len(listRefs) // 2 + 1 and len(listRefs) == 2 * k - 1:
        #     return head
        # if k > len(listRefs) // 2:
        #     k = len(listRefs) - k
        # listRefs[k - 2].next = listRefs[-k]
        # # temp = listRefs[-k].next
        # listRefs[-k].next = listRefs[k - 1].next
        # listRefs[-k - 1].next = listRefs[k - 1]
        # listRefs[k - 1].next = listRefs[1 - k]
        listRefs[k - 1], listRefs[-k] = listRefs[-k], listRefs[k - 1]
        dummy = start = ListNode(0)
        for node in listRefs:
            start.next = node
            start = start.next
            start.next = None
        return dummy.next
        
