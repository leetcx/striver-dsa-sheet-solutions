# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head==None:
            return None
        curr=head
        lesser=ListNode(-1)
        tail=lesser
        greater=ListNode(-1)
        greathead=greater

        while curr!=None:
            if curr.val<x:
                tail.next=curr
                tail=tail.next
                
            else:
                greathead.next=curr
                greathead=greathead.next
            curr=curr.next
        greathead.next=None
        tail.next=greater.next
        return lesser.next




