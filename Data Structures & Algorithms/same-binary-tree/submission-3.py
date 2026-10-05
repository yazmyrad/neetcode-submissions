# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if bool(p) ^ bool(q): return False
        if p and q and p.val != q.val: return False
        right, left = True, True
        if p and q:
            right = self.isSameTree(p.right, q.right)
            left =  self.isSameTree(p.left, q.left)

        return right and left