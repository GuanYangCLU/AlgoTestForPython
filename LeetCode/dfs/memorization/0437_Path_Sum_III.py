# https://leetcode.com/problems/path-sum-iii/discuss/141424/Python-step-by-step-walk-through.-Easy-to-understand.-Two-solutions-comparison.-%3A-)
# https://www.jiuzhang.com/problem/path-sum-iii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # total valid path count
        self.res = 0
        # memo of a specific pathSum value
        cache = {0:1}
        self.dfs(root, 0, targetSum, cache)
        return self.res
    
    def dfs(self, root, lastPathSum, targetSum, cache):
        if not root:
            return
        curPathSum = lastPathSum + root.val
        # we have stored some valid parents path sum
        # if curPathSum - parentsPathSum = targetSum, then we must have a slice of nodes valid
        sumStillNeedFromParentsPath = curPathSum - targetSum
        self.res += cache.get(sumStillNeedFromParentsPath, 0)
        # push this as valid parents path sum
        cache[curPathSum] = cache.get(curPathSum, 0) + 1
        
        self.dfs(root.left, curPathSum, targetSum, cache)
        self.dfs(root.right, curPathSum, targetSum, cache)
        
        # change to other side, cannot mix branch
        cache[curPathSum] -= 1
        
