# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def deep(node):
            if node==None:
                return 0,None
            leftdepth,leftnode=deep(node.left)
            rightdepth,rightnode=deep(node.right)

            if leftdepth==rightdepth:
                return ((leftdepth+1),node)
            elif leftdepth>rightdepth:
                return ((leftdepth+1),leftnode)
            else:
                return ((rightdepth+1),rightnode)
        depth,ans=deep(root)
        return ans