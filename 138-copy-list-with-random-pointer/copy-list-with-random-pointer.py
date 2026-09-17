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
        if head==None:
            return head
        curr=head
        prev=None
        copyhead=None
        while curr:
            p=Node(curr.val)
            if prev:
                prev.next=p
            else:
                copyhead=p
            prev=p
            curr=curr.next
        set1={}
        t=head
        g=copyhead
        while t:
            set1[t]=g
            g=g.next
            t=t.next
        t=head
        g=copyhead  
        while t:
            if t.random:
                g.random = set1[t.random]

            t = t.next
            g = g.next

        return copyhead
