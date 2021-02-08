"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm 
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    """
    def serialize(self, root):
        # write your code here
        if not root:
            return ''
        resList = []
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            resList.append(str(node.val) if node else '#')
            if node:
                queue.append(node.left)
                queue.append(node.right)
        return ','.join(resList)

    """
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    """
    def deserialize(self, data):
        # write your code here
        if not data:
            return
        nodeValueList = data.split(',')
        print(nodeValueList)
        nodeList = [TreeNode(int(val)) if val != '#' else None for val in nodeValueList]
        nodes, slow, fast = [nodeList[0]], 0, 1
        while slow < len(nodes):
            # slow point to current operating list
            node = nodes[slow]
            slow += 1
            # fast seek from data node list
            node.left = nodeList[fast]
            node.right = nodeList[fast + 1]
            fast += 2
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)
        return nodes[0]

# DFS:
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        return ','.join(self.getPreparedNodeList(root))
    
    def getPreparedNodeList(self, root):
        if not root:
            return ['#']
        return [str(root.val)] + self.getPreparedNodeList(root.left) + self.getPreparedNodeList(root.right)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        return self.dfs(data.split(','))
        
    def dfs(self, nodeList):
        nodeValStr = nodeList.pop(0)
        if nodeValStr == '#':
            return
        root = TreeNode(int(nodeValStr))
        root.left = self.dfs(nodeList)
        root.right = self.dfs(nodeList)
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
