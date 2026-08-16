# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def out(node):
            if node==None:
                return 0
            if node.left==None and node.right==None:
                return 1
            if node.left is None:
                return 1 + out(node.right)

            if node.right is None:
                return 1 + out(node.left)           
            leftdepth= out(node.left)
            rightdepth= out(node.right)
            return 1+min(leftdepth,rightdepth)
        return out(root)
            


        
        
        
        
        