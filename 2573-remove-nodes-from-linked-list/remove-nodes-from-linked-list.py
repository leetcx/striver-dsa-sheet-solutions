# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head ==None:
            return None
        curr=head
        st=[]
        while curr:
            while st and st[-1] < curr.val:
                st.pop()
            st.append(curr.val)
            curr=curr.next
        prev=None
        while st:
            d=ListNode(st.pop())
            d.next=prev
            prev=d
        return prev