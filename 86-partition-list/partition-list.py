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
        ans=ListNode(-1)
        tail=ans
        great=ListNode(-1)
        greater=great
        while curr!=None:
            if curr.val<x:
                tail.next=curr
                tail=tail.next
            else:
                greater.next=curr
                greater=greater.next
            curr=curr.next
        greater.next=None
        tail.next=great.next
        return ans.next