# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        left=list1
        right=list2
        dummy=ListNode(0)
        p=dummy

        while left and right:
            if left.val < right.val:
                p.next=left
                p=p.next
                left=left.next
            else:
                p.next=right
                p=p.next
                right=right.next
            
        while left:
            p.next=left
            p=p.next
            left=left.next
        while right:
            p.next=right
            p=p.next
            right=right.next
        return dummy.next


