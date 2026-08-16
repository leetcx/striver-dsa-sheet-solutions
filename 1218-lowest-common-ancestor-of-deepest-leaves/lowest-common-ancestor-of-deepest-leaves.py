# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def lca(node):
            if node==None:
                return 0,None
            leftdepth,leftnode=lca(node.left)
            rightdepth,rightnode=lca(node.right)

            if leftdepth==rightdepth:
                return (leftdepth+1),node
            if leftdepth>rightdepth:
                return (leftdepth+1),leftnode
            if rightdepth>leftdepth:
                return rightdepth+1,rightnode

        depth,ans= lca(root)
        return ans