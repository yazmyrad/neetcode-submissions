# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if n == 1 and not head.next:
            return None
        temp = head
        j = 0
        while temp:
            temp = temp.next
            j += 1
        prev = None
        curr = head
        i = 0
        while j-i>n:
            prev = curr
            curr = curr.next
            i += 1
        if prev:
            prev.next = curr.next
        else:
            head = head.next
        return head