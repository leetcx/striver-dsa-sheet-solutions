# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if root==  None:
            return 0
        st=[]
        st2=[]
        node=root
        de=root
        def getsmall():
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
            nonlocal de
            while de:
                st2.append(de)
                de=de.right
            i=st2.pop()
            big=i.left
            while big:
                st2.append(big)
                big=big.right
            return i
        m=getsmall()
        q=getbig()

        while m != q:
            if m.val + q.val == k:
                return True

            elif m.val + q.val < k:
                m = getsmall()

            else:
                q = getbig()

        return False
        
            