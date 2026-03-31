# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = prev = None

        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        
        second = prev
        first = head

        while second:
            nxtf, nxts = first.next, second.next
            first.next = second
            second.next = nxtf
            first, second = nxtf, nxts


