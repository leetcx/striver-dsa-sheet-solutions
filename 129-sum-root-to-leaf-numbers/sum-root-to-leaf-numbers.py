# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        p=0
        s=0
        def sum1(node):
            nonlocal p
            nonlocal s
            if node==None:
                return
            p=p*10+(node.val)
            if node.left ==None and node.right==None:
                s+=p

            sum1(node.left)
            sum1(node.right)
            p=p//10
        sum1(root)
        return s
            