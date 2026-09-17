# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow=head
        fast=head
        while fast and fast.next :
            slow=slow.next
            fast=fast.next.next
        p=slow
        second=p.next

        slow.next=None
        curr=second
        prev=None

        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        second=prev
        fast1=second
        slow1=head
        while fast1 and slow1:
            temp1=slow1.next
            temp2=fast1.next
            slow1.next=fast1
            fast1.next=temp1
            slow1 = temp1
            fast1 = temp2
        


        


