# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        curr=head
        smaller=ListNode(-1)
        small=smaller
        greater=ListNode(-1)
        great=greater
        while curr:
            if curr.val<x:
                small.next=curr
                small=small.next
            else:
                great.next=curr
                great=great.next
            curr=curr.next
        great.next=None
        small.next=greater.next
        return smaller.next