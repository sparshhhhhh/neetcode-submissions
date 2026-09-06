# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, currMax):
            if not node:
                return 0
            if node.val >= currMax:
                cnt = 1
                currMax = node.val
            else:
                cnt = 0
            cnt += dfs(node.left, currMax)
            cnt += dfs(node.right, currMax)
            return cnt
        return dfs(root, root.val)