# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        isValid = [True]
        def dfs(minNode, maxNode, node):
            if not(minNode < node.val < maxNode): 
                isValid[0] = False
                return
            if node.right:
                dfs(node.val, maxNode, node.right)
            
            if node.left:
                dfs(minNode, node.val, node.left)

            return 
        dfs(float('-inf'), float('inf'), root)
        return isValid[0]
            