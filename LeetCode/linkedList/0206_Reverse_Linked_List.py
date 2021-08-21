"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: n
    @return: The new head of reversed linked list.
    """
    def reverse(self, head):
        # write your code here
        # 链表和树的操作，都是局部操作维护整体的相似形 ★
        # 遍历过程中，始终保持链表切为两段，左边是倒序，存头指针，右边是正序尚未逆转，也存头指针
        # null | 1 -> 2 -> 3 -> null
        # null 1 | 2 -> 3 -> null
        # 1 -> null | 2 -> 3 -> null
        # 右头指针向后遍历，不断把旧的右头加到左头前面，始终严格维持这个状态
        left_head = None
        right_head = head
        while right_head:
            next_rihgt_head = right_head.next
            right_head.next = left_head
            left_head = right_head
            right_head = next_rihgt_head
        return left_head
