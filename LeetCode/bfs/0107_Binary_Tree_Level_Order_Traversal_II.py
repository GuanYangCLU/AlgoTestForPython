# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        distance = {root : 0}
        res = {0 : [root.val]}
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            if node.left:
                distance[node.left] = distance[node] + 1
                res[distance[node] + 1] = res.get(distance[node] + 1, []) + [node.left.val]
                queue.append(node.left)
            if node.right:
                distance[node.right] = distance[node] + 1
                res[distance[node] + 1] = res.get(distance[node] + 1, []) + [node.right.val]
                queue.append(node.right)
        resEntries = list(res.items())
        resEntries.sort(key = lambda tp : tp[0], reverse=True)
        return [lst for lv, lst in resEntries]
        
