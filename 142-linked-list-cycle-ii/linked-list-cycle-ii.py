# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast = head
        hascycle=False
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                hascycle=True
                break
        if not hascycle:
            return None
        fast=head
        while fast!=slow:
            fast=fast.next
            slow=slow.next
        return slow