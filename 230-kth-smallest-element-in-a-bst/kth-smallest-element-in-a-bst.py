# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], p: int) -> int:
        ans=[]
        def k(node):
            nonlocal ans
            if node==None:
                return 0
            k(node.left)
            ans.append(node.val)
            k(node.right)
        k(root)
        return ans[p-1]