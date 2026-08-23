# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def find(node):
            if node==None:
                return 
            if node.val == val:
                return node
            if val>node.val:
                return find(node.right)
            else:
                return find(node.left)

        return find(root)