# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        lst = []
        cur = head
        while cur:
            lst.append(cur.val)
            cur = cur.next
        return self.isPal(lst)
    
    def isPal(self, lst):
        if not lst or len(lst) < 2:
            return True
        left, right = 0, len(lst) - 1
        while left < right:
            if lst[left] != lst[right]:
                return False
            left += 1
            right -= 1
        return True
        
