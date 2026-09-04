# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow=head
        fast=head
        while fast !=None and fast.next !=None:
            slow=slow.next
            fast=fast.next.next
        curr=slow
        prev=None
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr

            curr=temp
        slow=head
        fast=prev
        while fast!=None:
            if slow.val !=fast.val:
                return False
            slow=slow.next
            fast=fast.next
        return True
        
           
            