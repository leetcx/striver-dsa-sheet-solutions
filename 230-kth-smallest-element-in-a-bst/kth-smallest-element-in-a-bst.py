# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans=[]
        def kth(node):
            nonlocal ans
            if node==None:
                return None
            kth(node.left)
            ans.append(node.val)
            kth(node.right)
        kth(root)
        return ans[k-1]

