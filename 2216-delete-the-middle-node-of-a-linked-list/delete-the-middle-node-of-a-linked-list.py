# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        c=0
        ans=ListNode(-1)
        twi=ans
        while curr!= None:
            c+=1
            curr=curr.next
        mid=c//2
        curr=head
        for i in range(0,c):
            if i!=mid:
                twi.next=curr
                twi=twi.next
                curr=curr.next
            else:
                curr=curr.next
        twi.next=None
        return ans.next
        
           

