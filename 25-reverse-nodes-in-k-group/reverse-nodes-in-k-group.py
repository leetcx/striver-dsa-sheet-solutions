# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,left,k):
        curr=left
        prev=None
        while curr and k>0:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
            k-=1
        return
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        left=head
        prevleft=None
        res=None
        while True:
            right=left
            for i in range(0,k-1):
                if right==None:
                    break
                right=right.next
            if right:
                nextleft=right.next
                self.reverse(left,k)
                if prevleft:
                    prevleft.next=right
                prevleft=left
                if res==None:
                    res=right
                left=nextleft
            else:
                if res==None:
                    res=left
                if prevleft:
                    prevleft.next=left
                break

        return res                    


