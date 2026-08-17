# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        ans=True
        def same(p,q):
            nonlocal ans
            if p==None and q==None:
                return True
            if p==None or q==None:
                ans=False
                return 
            if p.val != q.val:
                ans=False
                return
            same(p.left,q.left)
            same(p.right,q.right)
        def searchroot(r,sb):
            nonlocal ans

            if r==None:
                return None
            ans=False
            if r.val==sb.val:
                ans=True
                same(r,sb)
                if ans:
                    return
            searchroot(r.left,sb)
            if ans:
                return
            searchroot(r.right,sb)
        searchroot(root,subRoot)
        return ans