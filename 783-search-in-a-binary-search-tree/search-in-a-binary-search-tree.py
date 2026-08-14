# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def bst(node,val):
            if node==None:
                return None
            if node.val==val:
                return node

            if val>node.val:
                return bst(node.right,val)
            else:
               return bst(node.left,val)
        return bst(root,val)
      
            