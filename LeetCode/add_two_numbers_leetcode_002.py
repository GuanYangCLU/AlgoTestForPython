# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = int((''.join(map(str, self.readNum(l1))))[::-1])
        num2 = int((''.join(map(str, self.readNum(l2))))[::-1])
        # print(num1 + num2)
        
        
        # ans = num1 + num2
        # a = rs = ListNode(0)
        # while ans:
        #     rs.next = ListNode(ans%10)
        #     rs = rs.next
        #     ans = ans // 10
        # return a.next
    
    
        lst = list(str(num1+num2)[::-1])
        return self.writeNum(lst)
        
    def readNum(self, ln): # 解锁链
        lst = []
        while ln.next: 
            lst.append(ln.val)
            ln = ln.next
        lst.append(ln.val)
        return lst
                   
    def writeNum(self, lst): # 系锁链****
        # stack = [ListNode(0) for i in range(len(lst))]
        b = rs = ListNode(lst[0])       # b stay in start and rs start to run and continuing left rs.next
        for i in range(len(lst)):
            rs.next = ListNode(lst[i])  # under 3line method cannot create static linked list
            rs = rs.next                # cause no var was assigned to iterable value
            # stack.append(ListNode(lst[i]))
            # ListNode(lst[i]).next = ListNode(lst[i+1])
        return b.next