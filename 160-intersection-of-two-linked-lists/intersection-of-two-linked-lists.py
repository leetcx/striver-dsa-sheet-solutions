# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        left=headA
        right=headB
       
        while left!=right:
            
            
            if left==None:
                
                left=headB
            else:
                left=left.next
            if right==None:
                
                right=headA
            else:
                right=right.next
            
        return left