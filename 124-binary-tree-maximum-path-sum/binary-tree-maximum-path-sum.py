# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res=root.val
        def hu(node):
            nonlocal res
            
            if node==None:
                return 0
            leftmax=hu(node.left)
            rightmax=hu(node.right)
            leftmax=max(leftmax,0)
            rightmax=max(rightmax,0)

            res=max(res,node.val+leftmax+rightmax)
            return node.val+max(leftmax,rightmax)
        hu(root)
        return res