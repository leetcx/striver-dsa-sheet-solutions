# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        if head==None:
            return None
        curr=head
        count=0
        while curr:
            curr=curr.next
            count+=1
        d=count-n
        dummy=ListNode(0)
        dummy.next=head
        p=dummy
        while d>0:
            p=p.next
            d-=1
        if p and p.next:
            p.next=p.next.next
        return dummy.next
        
        


