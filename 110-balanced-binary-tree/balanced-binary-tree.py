# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ans=True
        def balance(node):
            nonlocal ans
            if node ==None:
                return 0
            a=balance(node.left)
            b=balance(node.right)
            if abs(a-b)>1:
                ans=False
            return 1+ max(a,b)
        balance(root)
        return ans
            
            