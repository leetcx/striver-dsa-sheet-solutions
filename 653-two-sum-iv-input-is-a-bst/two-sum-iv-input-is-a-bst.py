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
            
            
            p=st.pop()
                
            rightchild=p.right
            while rightchild:
                st.append(rightchild)
                rightchild=rightchild.left
            return p
            
        def getbig():
            
            nonlocal de
            while de:
                st2.append(de)
                de=de.right
            
            
            p=st2.pop()
                
            leftchild=p.left
            while leftchild:
                st2.append(leftchild)
                leftchild=leftchild.right
            return p
        i=getsmall()
        j=getbig() 
        while (i and j and i!=j and i.val<=j.val ):
            sum=i.val+j.val
            if sum==k:
                return True
            if sum>k:
                j=getbig()
            else:
                i=getsmall()
        return False   
          

        