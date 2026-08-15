# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        ans=None
      
        def value(node):
            
            nonlocal ans
            if node==None:
                return 0
            selfie=0
            if node==p or node==q:
                selfie=1
                
           
            left=value(node.left)
            right=value(node.right)
            total=selfie+left+right
            if total==2 and ans==None:
                ans = node
            return total
        value(root)
        return ans
            