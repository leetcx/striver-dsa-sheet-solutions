# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        st=[]
        st2=[]
        node=root
        de=root
        def getsmall():
            nonlocal node

            while node:
                st.append(node)
                node=node.left
            small=st.pop()
            leftsmall=small.right
            while leftsmall:
                st.append(leftsmall)
                leftsmall=leftsmall.left
            return small
        def getbig():
            nonlocal de
            while de:
                st2.append(de)
                de=de.right
            big=st2.pop()
            rightbig=big.left
            while rightbig:
                st2.append(rightbig)
                rightbig=rightbig.right
            return big
        i=getsmall()
        j=getbig()
        while (i and j and i!=j and i.val<=j.val):
            sum=i.val+j.val
            if sum==k:
                return True
            if sum>k:
                j=getbig()
            else:
                i=getsmall()
        return False
