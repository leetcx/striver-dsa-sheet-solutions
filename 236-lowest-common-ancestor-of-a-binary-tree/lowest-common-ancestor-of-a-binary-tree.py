# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans=0
        
       
        def seti(node,p,q):
            nonlocal ans
         
            selfi=0
            if node==None:
                return 0
            if node==p or node==q:
                selfi=1
            else:
                selfi=0
            
            left=seti(node.left,p,q)
            right=seti(node.right,p,q)
            total=selfi+left+right
            if total==2 and ans==0:
               
                ans=node
            return total
        seti(root,p,q)
        return ans
            
