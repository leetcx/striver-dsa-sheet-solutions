# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        c=0
        curr=head
        while curr:
            c+=1
            curr=curr.next
        k=k%c
        if k==0:
            return head
        slow=head
        prev=None
        for i in range(c-k):
            prev=slow
            slow=slow.next
        prev.next=None
        newhead=slow
        while slow.next:
            slow=slow.next
        slow.next=head
        
        return newhead

       
        
