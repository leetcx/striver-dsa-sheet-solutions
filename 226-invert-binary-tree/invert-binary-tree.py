# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def kriya(node):
            if node==None:
                return 
            if node.left==None and node.right ==None:
                return node
            else:
                node.left,node.right=node.right,node.left
            
            kriya(node.left)
            kriya(node.right)
        kriya(root)
        return root