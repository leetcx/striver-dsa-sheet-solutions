# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp=head
        count=0

        while count<k:
            if temp==None:
                return head
            temp=temp.next
            count+=1
        curr=head
        prev=None
        cnt=0

        while cnt<k:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
            cnt+=1
        head.next=self.reverseKGroup(curr,k)
        return prev