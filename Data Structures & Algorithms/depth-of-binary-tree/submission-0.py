# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxdepth = 0
        def dfs(depth, root):
            if root is None: return depth
            right, left = 0, 0
            if root.right:
                right = dfs(0, root.right)
            if root.left:
                left = dfs(0, root.left)
            return max(right, left) + 1
        
        return dfs(maxdepth, root)