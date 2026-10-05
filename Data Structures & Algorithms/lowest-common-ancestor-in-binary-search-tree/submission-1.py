# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def search(head):
            
            if min(p.val, q.val) <= head.val <= max(p.val, q.val): 
                return head
            if all([x < head.val for x in [p.val, q.val]]):
                return search(head.left)
            if all([x > head.val for x in [p.val, q.val]]): 
                return search(head.right)
        return search(root)