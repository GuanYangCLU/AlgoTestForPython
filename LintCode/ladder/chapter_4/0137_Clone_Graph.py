"""
class UndirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []
"""

class Solution:
    """
    @param node: A undirected graph node
    @return: A undirected graph node
    """
    def cloneGraph(self, node):
        # write your code here
        #thinking why use root = node
        root = node
        if not node:
            return node
            
        nodes = self.getNodes(node)
        
        cloneMap = {}
        for node in nodes:
            cloneMap[node] = UndirectedGraphNode(node.label)
            
        for node in nodes:
            new_node = cloneMap[node]
            for neighbor in node.neighbors:
                new_neighbor = cloneMap[neighbor]
                new_node.neighbors.append(new_neighbor)
                
        # wrong case: {-1,1#1} if use node
        return cloneMap[root]
                
    def getNodes(self, node):
        queue = collections.deque([node])
        results = set([node])
        while queue:
            head = queue.popleft()
            for n in head.neighbors:
                if n not in results:
                    results.add(n)
                    queue.append(n)
                    
        return results
        
