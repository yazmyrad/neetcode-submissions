"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hmap = {}
        curr = head
        while curr:
            hmap[curr] = Node(curr.val)
            curr = curr.next
        newhead = hmap[head] if head else None
        while head:
            hmap[head].next = hmap[head.next] if head.next else None
            hmap[head].random = hmap[head.random] if head.random else None
            head = head.next
        return newhead
            