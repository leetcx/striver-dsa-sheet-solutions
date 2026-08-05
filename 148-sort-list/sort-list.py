# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        slow=head
        fast=head
        ans=ListNode(-1)
        pri=ans

        prev=None

        while fast!=None and fast.next!=None:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        prev.next=None
        # Recursively sort both halves
        g = self.sortList(head)
        d = self.sortList(slow)

        while g!=None and d!=None:
            if g.val<=d.val:
                pri.next=g
                g=g.next
            else:
                pri.next=d
                d=d.next
            pri=pri.next

        if g!=None:
            pri.next=g
        else:
            pri.next=d
        return ans.next
