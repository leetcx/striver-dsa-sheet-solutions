# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res=[root.val]
        def maxi(node):
            nonlocal res
            if node==None:
                return 0
            leftmax=maxi(node.left)
            rightmax=maxi(node.right)
            leftmax=max(leftmax,0)
            rightmax=max(rightmax,0)

            res[0]=max(res[0],node.val+leftmax+rightmax)

            return node.val+max(leftmax,rightmax)
        maxi(root)
        return res[0]
            