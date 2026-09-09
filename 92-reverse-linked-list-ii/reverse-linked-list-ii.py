# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left==right:
            return head
        t=head
        pos=1
        before=None
        while t and pos<left:
            before=t
            t=t.next
            pos+=1
        if not t :
            return head
        
        prev=None
        curr=t
        z=right-left+1
        while z>0:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
            z-=1
        if before:
            before.next=prev
        else:
            head=prev
        t.next=curr
        
        return head
        