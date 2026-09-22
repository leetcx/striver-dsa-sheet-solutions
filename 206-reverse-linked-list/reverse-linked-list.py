# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        def rev(curr):
            if curr==None:
                return None
            if curr.next==None:
                return curr
            z=curr
            rest=rev(curr.next)
            p=rest
            while p and p.next:
                p=p.next
            if p:
                p.next=z
            z.next=None
            return rest
        return rev(head)    