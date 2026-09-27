# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def printList(self, head):
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        print(arr)

    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        pre_slow = None
        while fast:
            pre_slow = slow
            slow = slow.next
            if not fast.next: break
            fast = fast.next.next
        pre_slow.next = None
        
        prev = None
        curr = slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        first = head
        second = prev
        while second:
            temp1 = first.next
            temp2 = second.next
            
            first.next = second
            second.next = temp1

            first = temp1
            second = temp2
       
        
        