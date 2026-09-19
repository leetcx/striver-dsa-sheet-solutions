# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if root==None:
            return 0
        def maxdep(curr):
            if curr==None:
                return 0
            left=maxdep(curr.left)
            right=maxdep(curr.right)
            return 1+max(left,right)
        return maxdep(root)
