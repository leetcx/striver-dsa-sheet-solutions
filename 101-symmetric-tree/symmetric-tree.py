# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        chiesa=True
        def poly(left,right):
            nonlocal chiesa
            if left==None and right==None:
                return 
            if left==None or right==None:
                chiesa=False
                return
            if left.val!=right.val:
                chiesa=False
                return
            poly(left.left,right.right)
            poly(left.right,right.left)
        poly(root.left,root.right)
        return chiesa
