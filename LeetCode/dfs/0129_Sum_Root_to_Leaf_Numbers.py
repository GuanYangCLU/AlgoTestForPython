# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(node, cur, res):
            if node:
                cur += str(node.val)
                if not node.left and not node.right:
                    res.append(int(cur))
                else:
                    dfs(node.left, cur, res)
                    dfs(node.right, cur, res)
            else:
                return
            
        res = []
        dfs(root, '', res)
        return sum(res)
        
