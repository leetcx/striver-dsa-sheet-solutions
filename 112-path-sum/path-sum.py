# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        h=False

        def path(node,sum):
            nonlocal h
            if node==None:
                return 
            sum=sum+node.val
            if node.left==None and node.right==None:
                if sum==targetSum:
                    h=True
                    return
            path(node.left,sum)
            path(node.right,sum)
        path(root, 0)
        return h
        
            