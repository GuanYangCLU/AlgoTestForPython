# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        stackA, stackB = [], []
        self.fillStack(stackA, headA)
        self.fillStack(stackB, headB)
        res = None
        while stackA and stackB:
            lastA, lastB = stackA.pop(), stackB.pop()
            if lastA != lastB:
                break
            res = lastA
        return res         

    def fillStack(self, stack, head):
        cur = head
        while cur:
            stack.append(cur)
            cur = cur.next
            
