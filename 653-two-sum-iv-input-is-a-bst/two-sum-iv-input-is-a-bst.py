# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if root==None:
            return None
        st=[]
        st2=[]
        node=root
        de=root
        def getsmall():
            nonlocal st
            nonlocal node
            while node:
                st.append(node)
                node=node.left
            p=st.pop()
            small=p.right
           
            while small:
                st.append(small)
                small=small.left
            return p
        def getbig():
            nonlocal st2
            nonlocal de
            while de:
                st2.append(de)
                de=de.right
            q=st2.pop()
            big=q.left
            
            while big:
                st2.append(big)
                big=big.right
            return q
        i=getsmall()
        j=getbig()
        while i!=j:
            if i.val+j.val==k:
                return True
            if i.val+j.val>k:
                j=getbig()
            else:
                i=getsmall()
        return False