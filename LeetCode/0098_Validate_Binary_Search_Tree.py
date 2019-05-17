# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.lst = []
    def isValidBST(self, root: TreeNode) -> bool:
        if not root: return True
        self.helper(root)
        print(self.lst)
        for i in range(1,len(self.lst)):
            if sorted(self.lst)[i] == sorted(self.lst)[i-1]:
                return False
        return self.lst == sorted(self.lst)
   
    def helper(self, root):
        if not root.left and not root.right: 
            self.lst.append(root.val)
        if root.left:
            self.helper(root.left)
        if root.left or root.right:
            self.lst.append(root.val)
        if root.right:
            self.helper(root.right)


# OTHER
class Solution(object):
    def isValidBST(self, root):
        return self.helper(root, -float('inf'), float('inf'))
    
    def helper(self, node, lower_bound, upper_bound):
        if not node: return True
        if node.val >= upper_bound or node.val <= lower_bound:
            return False
        left = self.helper(node.left, lower_bound, node.val)
        right = self.helper(node.right, node.val, upper_bound)
        return left and right

class Solution(object):
    def isValidBST(self, root):
        self.arr = []
        self.inorder(root)
        return self.arr == sorted(self.arr) and len(self.arr) == len(set(self.arr))
    
    def inorder(self, root):
        if not root: return
        self.inorder(root.left)
        self.arr.append(root.val)
        self.inorder(root.right)
        
class Solution(object):
    def isValidBST(self, root):
        self.last = -float('inf')
        self.flag = True
        self.inorder(root)
        return self.flag
    
    def inorder(self, root):
        if not root: return
        self.inorder(root.left)
        if self.last >= root.val:
            self.flag = False
        self.last = root.val
        self.inorder(root.right)
