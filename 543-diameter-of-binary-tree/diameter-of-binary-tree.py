# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res=0
        def dia(node):
            nonlocal res
            if node==None:
                return 0
            a=dia(node.left)
            b=dia(node.right)
            sum1=a+b
            res=max(sum1,res)
            return 1 + max(a,b)
        dia(root)
        return res
