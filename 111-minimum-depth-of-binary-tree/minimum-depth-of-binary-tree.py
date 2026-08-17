# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def min2(node):
            if node==None:
                return 0
            if node.left==None:
                return 1+min2(node.right)
            elif node.right==None:
                return 1+ min2(node.left)
            p=min2(node.left)
            g=min2(node.right)
            return 1+min(p,g)
        return min2(root)