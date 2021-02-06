"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root
    @return: the second minimum value in the set made of all the nodes' value in the whole tree
    """
    def findSecondMinimumValue(self, root):
        # Write your code here
        # use ref to keep value and modify
        second = [float('inf')]
        rootVal = root.val
        self.findSecond(root, second, rootVal)
        return -1 if second[0] == float('inf') else second[0]
        
    def findSecond(self, node, second, rootVal):
        if not node:
            return
        if rootVal < node.val < second[0]:
            second[0] = node.val
        self.findSecond(node.left, second, rootVal)
        self.findSecond(node.right, second, rootVal)


class Solution:
    """
    @param root: the root
    @return: the second minimum value in the set made of all the nodes' value in the whole tree
    """
    def findSecondMinimumValue(self, root):
        # Write your code here
        values = set()
        self.pushValue(root, values)
        uniqueValues = sorted(list(values))
        return -1 if len(uniqueValues) < 2 else uniqueValues[1]
        
    def pushValue(self, node, values):
        if not node:
            return
        values.add(node.val)
        self.pushValue(node.left, values)
        self.pushValue(node.right, values)
