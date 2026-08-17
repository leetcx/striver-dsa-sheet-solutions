# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        def inord(node):
            nonlocal ans
            if node==None:
                return None
            inord(node.left)
            ans.append(node.val)
            inord(node.right)
        inord(root)
        return ans