# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        g=True
        def check(p1,q1):
            nonlocal g
            if p1==None and q1==None:
                return
            if p1==None or q1==None:
                g=False
                return
            if p1.val != q1.val:
                g=False
                return
            
            check(p1.left,q1.left)
            check(p1.right,q1.right)
        check(p,q)
        return g
