"""
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        # write your code here
        if not graph:
            return []
        
        indegrees = self.getIndegree(graph)
        zero_indegree_nodes = [n for n in indegrees if indegrees[n] == 0]
        queue = collections.deque(zero_indegree_nodes)
        res = []
        while queue:
            node = queue.popleft()
            res.append(node)
            for neighbor in node.neighbors:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)
        return res
        
    def getIndegree(self, graph):
        indegree = { n: 0 for n in graph }
        for node in graph:
            for neighbor in node.neighbors:
                indegree[neighbor] += 1
        return indegree
