# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root==None:
            return True
        ans=True
        def check(n1,n2):
            nonlocal ans
            if n1 ==None and n2==None:
                return True
            if n1==None or n2==None:
                ans=False
                return
            if n1.val != n2.val:
                ans=False
                return
            check(n1.left,n2.right)
            check(n1.right,n2.left)
        check(root.left,root.right)
        return ans
        
            