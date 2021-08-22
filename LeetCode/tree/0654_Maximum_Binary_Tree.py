# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        return self.buildTree(nums)
        
    def buildTree(self, subList):
        if not subList:
            return
        maxVal = max(subList)
        maxIdx = subList.index(maxVal)
        leftSub, rightSub = [], []
        if maxIdx > 0:
            leftSub = subList[:maxIdx]
        if maxIdx < len(subList) - 1:
            rightSub = subList[maxIdx + 1:]
        node = TreeNode(maxVal)
        node.left = self.buildTree(leftSub)
        node.right = self.buildTree(rightSub)
        return node
        
