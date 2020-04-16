# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res1 = []
        res2 = []
        def getNum(node, res):
            if node.next:
                res.append(str(node.val))
                return getNum(node.next, res)
            else:
                res.append(str(node.val))
                return int((''.join(res))[::-1])
        res = str(getNum(l1, res1) + getNum(l2, res2))[::-1]
        print(res)
        root = ListNode(0)
        def helper(node, idx, res):
            if not node:
                return
            node.val = res[idx]
            if idx < len(res) - 1:
                node.next = ListNode(res[idx+1])
            helper(node.next, idx + 1, res)
        helper(root, 0, res)
        return root
       
