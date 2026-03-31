# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        i = 0
        curr1 = l1
        curr2 = l2
        num = 0
        while curr1 or curr2:
            a = curr1.val * (10**i) if curr1 else 0
            b = curr2.val * (10**i) if curr2 else 0

            num += a + b

            curr1 = curr1.next if curr1 else None
            curr2 = curr2.next if curr2 else None
            i+=1

        res = curr = ListNode()

        while num:
            curr.val = num % 10
            num = num//10
            curr.next = ListNode() if num > 0 else None
            curr = curr.next

        return res





        
        
