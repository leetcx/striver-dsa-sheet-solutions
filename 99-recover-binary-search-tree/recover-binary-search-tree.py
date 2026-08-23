# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prev=None
        galat=0
        g1=0
        g2=0
        s1=0
        s2=0
        def recov(node):
            nonlocal prev
            nonlocal g1
            nonlocal g2
            nonlocal s1
            nonlocal s2
            nonlocal galat
            if node==None:
                return None
            recov(node.left)

            if prev !=None and prev.val>node.val:
                if galat==0:
                    galat+=1
                    g1=prev
                    g2=node
                elif galat==1:
                    galat+=1
                    s1=prev
                    s2=node
                   
            prev=node
            

           
            
            recov(node.right)
            
                    
           
        recov(root)
        if galat == 1:
            g1.val, g2.val = g2.val, g1.val
        else:
            g1.val, s2.val = s2.val, g1.val
         
        
            