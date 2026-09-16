# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        if head==None:
            return head
        dummy=ListNode(0)
        dummy.next=head
        slow=dummy
        for i in range(left-1):
            if slow:
                slow=slow.next
        d=slow
        fast=head
        
        for i in range(right):
            if fast:
                fast=fast.next
                
        curr=slow.next
        end=curr 
        prev=None
        while curr != fast:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        d.next=prev
        end.next=fast
        return dummy.next
        