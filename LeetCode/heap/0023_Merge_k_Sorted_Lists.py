# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        dummy = head = ListNode(0)
        buffer = []
        # init buffer
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(buffer, (lists[i].val, i))
                lists[i] = lists[i].next
        while buffer:
            value, nextIndex = heapq.heappop(buffer)
            head.next = ListNode(value)
            head = head.next
            if lists[nextIndex]:
                heapq.heappush(buffer, (lists[nextIndex].val, nextIndex))
                lists[nextIndex] = lists[nextIndex].next
        return dummy.next
        
