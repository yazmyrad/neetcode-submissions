# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        goodNodes = []
        def dfs(maxNode, node):
            if node is None: return
            if node.val >= maxNode: 
                goodNodes.append(node.val)
            if node.right: 
                dfs(max(maxNode, node.val), node.right)
            if node.left: 
                dfs(max(maxNode, node.val), node.left)
            return
        dfs(root.val, root)
        return len(goodNodes)