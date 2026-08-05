# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head==None or head.next ==None:
            return None
        p=head
        s=head

        for i in range(n):
            s=s.next
        if s==None:
            return head.next
        while s.next!=None:
            s=s.next
            p=p.next
        p.next=p.next.next
        return head