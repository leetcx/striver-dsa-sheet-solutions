# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        if head==None:
            return True
        slow=head
        fast=head
        while fast and fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        
        p=slow
        second=p.next
        p.next=None
        d=second
        prev=None
        while d:
            temp=d.next
            d.next=prev
            prev=d
            d=temp
        second=prev
        g=second
        t=head
        while g and t:
            if g.val != t.val:
                return False
            g=g.next
            t=t.next
        return True
        