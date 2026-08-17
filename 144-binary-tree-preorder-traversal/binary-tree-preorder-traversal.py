# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        def inord(node):
            nonlocal ans
            if node==None:
                return None
           
            ans.append(node.val)
            inord(node.left)
            inord(node.right)
        inord(root)
        return ans