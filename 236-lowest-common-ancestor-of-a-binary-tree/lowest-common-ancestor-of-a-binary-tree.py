# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans=None
        def lca(node):
            selfi=0
            nonlocal ans
            if node==None:
                return 0
            if node==p or node==q:
                selfi=1
            left=lca(node.left)
            right=lca(node.right)
            total=selfi+left+right
            if total==2 and ans==None:
                ans=node
            return total
        lca(root)
        return ans
            
