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
        ll = []
        curr = head
        while curr:
            ll.append(Node(curr.val))
            curr = curr.next
        ll.append(None)
        
        curr = head

        for i in range(len(ll)-1):
            if curr.random:
                index = len(ll)-1
                tmp = curr.random
                while tmp:
                    tmp = tmp.next
                    index-=1
                ll[i].random = ll[index]
            ll[i].next = ll[i+1]
            curr = curr.next
        
        return ll[0]

            
                














