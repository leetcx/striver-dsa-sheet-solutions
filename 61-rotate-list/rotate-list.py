# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        l=0
        curr=head
        while curr:
            l+=1
            curr=curr.next
        k = k % l

        if k == 0:
            return head
        p=head
        for i in range(l-k-1):
            if p==None:
                break
            p=p.next
        d=p.next
        p.next=None
       
        curr1=d
        while curr1.next:
            curr1=curr1.next
        curr1.next=head
        return d
        
     
        

