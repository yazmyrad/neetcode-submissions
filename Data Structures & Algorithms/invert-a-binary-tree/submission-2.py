# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return root
        q = deque()
        seen = set()
        q.append(root)
        while q:
            node = q.popleft()
            if node in seen:
                continue
            temp = node.left
            node.left = node.right
            node.right = temp
            seen.add(node)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        return root
