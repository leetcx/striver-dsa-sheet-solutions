# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        curr=head
        ans=ListNode(-1)
        tail=ans
        large=ListNode(-1)
        largetail=large
        while curr!=None:
            if curr.val<x:
                tail.next=curr
                tail=tail.next
            else:
                largetail.next=curr
                largetail=largetail.next
            curr=curr.next
        largetail.next = None
        tail.next=large.next
        return ans.next
        
        
