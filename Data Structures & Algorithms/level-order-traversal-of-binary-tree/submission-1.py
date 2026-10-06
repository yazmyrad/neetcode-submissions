# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        q = deque([root])
        levels = [[root.val]]
        while q:
            level = []
            while q:
                node = q.popleft()
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)               
                
            if level: levels.append([node.val for node in level])
            q = deque(level)
        return levels