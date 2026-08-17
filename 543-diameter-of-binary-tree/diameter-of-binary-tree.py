# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res=0
        def mij(node):
            nonlocal res
            if node==None:
                return 0
            p=mij(node.left)
            q=mij(node.right)
            sum1=p+q
            res=max(res,sum1)
            return 1+max(p,q)
        mij(root)
        return res