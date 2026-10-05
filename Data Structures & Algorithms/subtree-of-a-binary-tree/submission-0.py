# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isEqual(p, q):
            if q is None and p is None: return True
            if bool(p) ^ bool(q): return False
            if p.val != q.val: return False
            right = isEqual(p.right, q.right)
            left = isEqual(p.left, q.left)
            return right and left
        ans = False
        def dfs(node):
            nonlocal ans
            if node is None: return
            
            if node.val == subRoot.val and not ans:
                ans = isEqual(node, subRoot)
            
            if node.right: dfs(node.right)
            if node.left: dfs(node.left)
            return 
        dfs(root)
        return ans

            