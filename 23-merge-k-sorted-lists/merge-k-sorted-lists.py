# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
    
        while len(lists)>1:
            ans=[]
            for i in range(0,len(lists),2):
                l1=lists[i]
                l2=lists[i+1] if i+1<len(lists) else None
                ans.append(self.mergetwolist(l1,l2))
            lists=ans
        return lists[0]

    def mergetwolist(self,l1,l2):
        dummy=ListNode(-1)
        tail=dummy

        while l1!=None and l2!=None:
            if l1.val < l2.val:
                tail.next=l1
                tail=tail.next
                l1=l1.next
            else:
                tail.next=l2
                tail=tail.next
                l2=l2.next
        if l1:
            tail.next=l1
        if l2:
            tail.next=l2
        return dummy.next


        
