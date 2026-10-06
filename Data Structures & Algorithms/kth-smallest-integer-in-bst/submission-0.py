# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        hp = []
        def dfs(node):
            if node is None: return
            if len(hp) == k: 
                return
            #print(node.val, hp)
            dfs(node.left)
            heapq.heappush(hp, node.val)
            dfs(node.right)
            return
        dfs(root)
        for _ in range(k-1):
            heapq.heappop(hp)
        return heapq.heappop(hp)