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
        def val(node):
            nonlocal prev
            nonlocal ans
            if node==None:
                return True
            val(node.left)
            if prev!=None and prev.val>=node.val:
                ans=False
                return
            prev=node
            
            val(node.right)
        val(root)
        return ans