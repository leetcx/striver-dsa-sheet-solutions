# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        h=False

        def path(node,sum1):
            nonlocal h
            if node==None:
                return None
            sum1+=node.val
            if node.left==None and node.right==None:
                if sum1==targetSum:
                    h=True
                    return
            path(node.left,sum1)
            path(node.right,sum1)
        
        path(root,0)
        return h