# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        cutStart = cutEnd = list1
        stepToA, stepToB = a, b
        cutStart, cutEnd = self.getNodeByIndex(cutStart, stepToA - 1), self.getNodeByIndex(cutEnd, stepToB + 1)
        cur = list2
        while cur.next:
            cur = cur.next
        cutStart.next = list2
        cur.next = cutEnd
        return list1
        
    def getNodeByIndex(self, node, distance):
        cur = node
        while distance > 0:
            cur = cur.next
            distance -= 1
        return cur
      
