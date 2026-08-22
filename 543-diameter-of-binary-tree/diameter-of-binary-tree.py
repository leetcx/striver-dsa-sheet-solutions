# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res=0
        def dep(node):
            nonlocal res
            if node==None:
                return 0
            left=dep(node.left)
            right=dep(node.right)
            sum=left+right
            res=max(res,sum)
            return 1+max(left,right)
        dep(root)
        return res