# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxdiam = [0]
        def dfs(node):
            if node is None: return 0
            left, right = 0, 0
            if node.left: left = dfs(node.left)
            if node.right: right = dfs(node.right)
            maxdiam[0] = max(maxdiam[0], left+right)
            return max(left, right) + 1

        dfs(root)
        return maxdiam[0]