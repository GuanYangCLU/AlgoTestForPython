"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
# class UndirectedGraphNode:
    # def __init__(self, x):
        # self.label = x
        # self.neighbors = []
# 提交通过的正解，注意参考的UndirectedGraphNode的定义，结合题目里Node的不同定义 
# 定义地址： https://leetcode.com/problems/clone-graph/discuss/166603/Python-DFS-BFS
# 参考地址： https://leetcode.com/problems/clone-graph/discuss/42354/Python-DFS-short-solution
       
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return node
        root = Node(node.val, [])
        stack = [node]
        visit = {}
        visit[node.val] = root
        while stack:
            top = stack.pop()
            for n in top.neighbors:
                if not n.val in visit: 
                    stack.append(n)
                    visit[n.val] = Node(n.val, [])                    
                visit[top.val].neighbors.append(visit[n.val])
        return root

        
'''
# 其他人给的参考    
def cloneGraph(node):
    if not node:
        return node
    root = UndirectedGraphNode(node.label)
    stack = [node]
    visit = {}
    visit[node.label] = root
    while stack:
        top = stack.pop()
    
        for n in top.neighbors:
            if n.label not in visit:
                stack.append(n)
                visit[n.label] = UndirectedGraphNode(n.label)
            visit[top.label].neighbors.append(visit[n.label])
    
    return root
    
# input {"$id":"1","neighbors":[{"$id":"2","neighbors":[{"$ref":"1"},{"$id":"3","neighbors":[{"$ref":"2"},{"$id":"4","neighbors":[{"$ref":"3"},{"$ref":"1"}],"val":4}],"val":3}],"val":2},{"$ref":"4"}],"val":1}

'''
