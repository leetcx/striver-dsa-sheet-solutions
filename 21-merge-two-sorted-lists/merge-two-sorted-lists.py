# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1=list1
        l2=list2
        ans=ListNode(-1)
        tail=ans
        while l1 and l2:
            if l1.val<=l2.val:
                tail.next=l1
                l1=l1.next
            elif l2.val<l1.val:
                tail.next=l2
                l2=l2.next
            tail=tail.next

        while l1:
            tail.next=l1
            tail=tail.next
            l1=l1.next
        
        while l2:
            tail.next=l2
            tail=tail.next
            l2=l2.next
        return ans.next
        
