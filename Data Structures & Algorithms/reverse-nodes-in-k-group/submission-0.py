# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        size = 0
        curr = head

        while curr:
            curr = curr.next
            size+=1
    
        curr = head
        trailing_node1 = curr
        for i in range(size//k):
            prev = self.nxt_node(curr, k)
            trailing_node_2 = curr
            for a in range(k):
                if not curr:
                    break
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            if i == 0:
                head = prev
            else:
                trailing_node1.next = prev
                trailing_node1 = trailing_node_2
        
        return head

    def nxt_node(self, head, k):
        dummy = head
        for i in range(k):
            dummy = dummy.next
        return dummy