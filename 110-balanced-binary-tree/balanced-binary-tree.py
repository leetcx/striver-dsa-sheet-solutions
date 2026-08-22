# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ans=True
        def bal(node):
            nonlocal ans
            if node==None:
                return 0
            p=bal(node.left)
            c=bal(node.right)
            
            if abs(p-c)>1:
                ans=False
             
            return 1+ max(p,c)

        bal(root)
        return ans