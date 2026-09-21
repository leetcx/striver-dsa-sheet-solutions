# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, p: TreeNode | None, q: TreeNode | None) -> TreeNode | None:
        def merge(p,q):
            if p==None:
                return q
            if q==None:
                return p
            p.val+=q.val
            p.left=merge(p.left,q.left)
            p.right=merge(p.right,q.right)
            return p
        return merge(p,q)