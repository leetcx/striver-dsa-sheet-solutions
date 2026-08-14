# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def tio(node):
            if node==None:
                return 0
            if node.left==None and node.right==None:
                return 1
            if node.left==None:
                return 1+ tio(node.right)
            if node.right==None:
                return 1+ tio(node.left)
            p=tio(node.left)
            g=tio(node.right)
            return 1+min(p,g)

        return tio(root)
