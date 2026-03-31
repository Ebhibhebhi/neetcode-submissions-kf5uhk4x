# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        dummy = ListNode()
        for i in range(len(lists) - 1):
            curr = dummy
            first, second = lists[i], lists[i+1]
            while first and second:
                if first.val <= second.val:
                    curr.next = first
                    first = first.next
                else:
                    curr.next = second
                    second = second.next
                curr = curr.next
            if first:
                curr.next = first
            elif second:
                curr.next = second
            lists[i+1] = dummy.next

        return dummy.next




