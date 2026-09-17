# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,left,t):
        curr=left
        prev=None
        while curr and t>0:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
            t-=1
        return prev,left
        
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        left=head
        prevleft=None
        res=None
        while True:
            right=left
            for i in range(k-1):
                if right:
                    right=right.next
                else:
                    break
            if right:
                nextleft=right.next
                newhead,tail=self.reverse(left,k)
                if prevleft:
                    prevleft.next=newhead
                prevleft=tail
                prevleft.next=nextleft

                left=nextleft
                
                if res==None:
                    res=newhead
            else:
                if res==None:
                    res=left
                else:
                    if prevleft:
                        prevleft.next=left
                break
        return res
                