# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        res = {}       
        def dfs(node):
            if node:
                res[node.val] = res.get(node.val, 0) + 1
                dfs(node.left)
                dfs(node.right)
        try:
            dfs(root)
            modeNum = max(res.values())
            return [k for k in res.keys() if res[k] == modeNum]
        except:
            return []

```
JavaScript time limit, why?
var findMode = function(root) {
    if (!root) return [];
    let res = {};
    const helper = (node) => {
        if (!node) return;
        res = { ...res, [node.val]: res[node.val] ? res[node.val] + 1 : 1 };
        helper(node.left, res);
        helper(node.right, res);
    }
    helper(root, res);
    const modeNum = Math.max(...Object.values(res));
    return Object.entries(res).filter(([key, value]) => value === modeNum).map(([key, value]) => key);
};
```
