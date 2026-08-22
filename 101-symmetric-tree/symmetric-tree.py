# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        ans=True
        def check(left,right):
            nonlocal ans
           
            if left==None and right==None:
                return True
            if left==None or right==None:
                ans=False
                return
            if left.val != right.val:
                ans=False
            check(left.left,right.right)
            check(left.right,right.left)

        check(root.left,root.right)
        return ans