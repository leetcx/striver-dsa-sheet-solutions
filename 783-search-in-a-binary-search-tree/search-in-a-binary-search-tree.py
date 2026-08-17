# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def value(node,val):
            if node==None:
                return None
            if node.val==val:
                return node
            if node.val>val:
                return value(node.left,val)
            else:
                return value(node.right,val)
        return value(root,val)
       

            
            