# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        ans=True
        def same(p1,q1):
            nonlocal ans
            if p1==None and q1==None:
                return True
            if p1==None or q1==None:
                ans=False
                return
            if p1.val != q1.val:
                ans=False
                return
            same(p1.left,q1.left)
            same(p1.right,q1.right)
        same(p,q)
        return ans