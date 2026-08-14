# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans=[]
        def lowest(node,p,q):
            nonlocal ans
            if node==None:
                return 0
            a=lowest(node.left,p,q)
            b=lowest(node.right,p,q)
            self=0
            if node==p or node==q:
                self=1
            total=a+b+self
            if total==2 and ans==[]:
                ans=node
            return total
        lowest(root,p,q)
        return ans
            

        