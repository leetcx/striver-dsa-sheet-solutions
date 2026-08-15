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
        g1=None
        galat=0
        g2=None
        s1=None
        s2=None
        prev=None
        def fun(node):
            nonlocal g1
            nonlocal galat
            nonlocal g2
            nonlocal s1           
            nonlocal s2
            nonlocal prev
            if node== None:
                return None
            fun(node.left)
           
            if prev!=None and prev.val> node.val:
                if galat==0:
                    g1=prev
                    g2=node
                    galat+=1
                else:
                    s1=prev
                    s2=node
                    galat+=1
            prev=node
            fun(node.right)
        fun(root)
        if galat==2:
            g1.val,s2.val=s2.val,g1.val
        else:
            g1.val,g2.val=g2.val,g1.val

