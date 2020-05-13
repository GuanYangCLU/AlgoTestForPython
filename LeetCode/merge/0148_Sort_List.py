# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # practice bottom up concept
        def getSize(head):
            size = 0
            while head:
                size += 1
                head = head.next
            return size
        # cut off linked list, get length and return the rest list's head; Care about not enough length
        def split(head, size):
            idx = 1
            while idx < size and head: # protection cover the case when rest size is not enough
                idx += 1                
                head = head.next
            newHead = None
            if head:
                newHead = head.next
                head.next = None # cut off here
            return newHead
        # merge first section(left) with size n and second section(right) with maybe size n, return tail node of merged results
        def merge(left, right, prevMergedTail):
            cur = prevMergedTail # init to start merge 2 sections
            while left and right: # any side empty, stop and continue single side till end
                if left.val > right.val:
                    cur.next = right
                    right = right.next # move an item from right section to merged section
                else:
                    cur.next = left
                    left = left.next
                cur = cur.next # keep iterate index
            cur.next = right if not left else left # for rest section, just part of left or right, iterate till its end
            while cur.next:
                cur = cur.next
            return cur
        # use these functions to bottom up merge
        if not head:
            return
        size = getSize(head)
        left, right, initMergedTail = None, None, None
        dummy = ListNode(0)
        dummy.next = head
        bottomSize = 1 # on bottom level, start with 1 item per section
        while bottomSize < size:
            initMergedTail = dummy
            cur = dummy.next # init as head every time finishing a merge for size 2**n
            while cur:
                left = cur
                right = split(left, bottomSize)
                cur = split(right, bottomSize) # must first calculate the cur index and then merge
                initMergedTail = merge(left, right, initMergedTail) # one time just used size + size length, keep until iterate whole length
            bottomSize *= 2
        return dummy.next
   
