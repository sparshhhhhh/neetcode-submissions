# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        d = 0
        def dfs(node, d):
            if not node:
                return d
            return 1 + max(dfs(node.left, d), dfs(node.right, d))
        return dfs(root, d)