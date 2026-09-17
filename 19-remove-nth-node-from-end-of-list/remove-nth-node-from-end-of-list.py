# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        
        dummy=ListNode(0)
        dummy.next=head
        slow=dummy
        fast=dummy
        while fast and n>0:
            fast=fast.next
            
            n-=1
        if fast==None:
            return None
        
        while fast and fast.next:
            slow=slow.next
            fast=fast.next
        if slow:
            slow.next=slow.next.next
        return dummy.next