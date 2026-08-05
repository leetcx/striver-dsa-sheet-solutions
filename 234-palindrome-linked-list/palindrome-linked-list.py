# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        set1=[]
        p=head

        while p !=None:
            set1.append(p.val)
            p=p.next
        curr=head
        prev=None
        next=None
        while curr!=None:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        curr=prev
        i=0

        while curr!=None:
            if curr.val != set1[i]:

                return False
            else:
                curr=curr.next
                i=i+1
        return True
