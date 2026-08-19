# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        ans=None
        def lca(node,p,q):
            selfi=0
            total=0
            nonlocal ans
            if node==None:
                return 0
            if node==p or node==q:
                selfi=1
            else:
                selfi=0
            left=lca(node.left,p,q)
            right=lca(node.right,p,q)
            total+=selfi + left + right
            if total == 2 and ans==None:
                ans=node
            return total
        lca(root,p,q)
        return ans
        
