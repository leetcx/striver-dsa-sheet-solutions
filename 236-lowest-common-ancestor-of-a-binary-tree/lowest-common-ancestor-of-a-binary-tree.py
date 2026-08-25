# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans=None
        
        def tui(node):
            nonlocal ans
            if node==None:
                return 0
           
            if node==p or node==q:
                selfi=1
            else:
                selfi=0
            left=tui(node.left)
            right=tui(node.right)
            total=left+right+selfi
            
            if total==2 and ans==None:
                ans = node
            return total
                
        tui(root)
        return ans
            