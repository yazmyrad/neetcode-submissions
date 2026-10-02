# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0
        q = deque()
        depth = 0
        q.append(root)
        while q:
            size = len(q)
            while size:
                node = q.popleft() 
                size -= 1
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            depth += 1
        return depth