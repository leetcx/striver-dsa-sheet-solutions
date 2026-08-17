# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans=[]
        def lca(node,p,q):
            nonlocal ans
            if node==None:
                return 0
            if node==p or node==q:
                ans=node
              
            if node.val>p.val and node.val>q.val:
                lca(node.left,p,q)
            elif node.val<p.val and node.val<q.val:
                lca(node.right,p,q)
            else:
                ans=node
               
        lca(root,p,q)
        return ans