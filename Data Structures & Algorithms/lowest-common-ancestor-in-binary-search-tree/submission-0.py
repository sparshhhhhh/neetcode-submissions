# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val < q.val:
            s = p.val
            b = q.val
        else:
            s = q.val
            b = p.val
        def dfs(node, s, b):
            if node.val >= s and node.val <= b:
                return node
            if node.val > b:
                return dfs(node.left, s, b)
            if node.val < s:
                return dfs(node.right, s, b)
        return dfs(root, s, b)