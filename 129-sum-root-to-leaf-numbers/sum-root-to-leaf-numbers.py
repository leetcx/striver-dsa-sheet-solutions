# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        sum1=0
        p=0
        def de(node):
            nonlocal sum1
            nonlocal p
            if node==None :
                return 0
            p=p*10+(node.val)
            if node.left ==None and node.right==None:
                sum1+=p
            de(node.left)
            de(node.right)
            p=p//10
        de(root)
        return sum1