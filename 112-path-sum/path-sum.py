# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        ans=False
        def pathy(node,sum1):
           
            
            nonlocal ans
            if node == None:
                return False
            sum1+=node.val
            if sum1==targetSum and node.left==None and node.right==None:
                ans=True
            pathy(node.left,sum1)
            pathy(node.right,sum1)
        pathy(root,0)
        return ans
        