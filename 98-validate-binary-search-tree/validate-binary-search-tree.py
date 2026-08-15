# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev=None
        ans=True
        def valid(node):
            nonlocal ans
            nonlocal prev
            if node == None:
                return True
            valid(node.left)
            
            if prev !=None and node.val<=prev.val:
                ans= False
            prev=node
            valid(node.right)
        valid(root)
        return ans
      