# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        cal=0
        path=[]
        def good(node):
            nonlocal cal
            if node==None:
                return 0
            path.append(node.val)

            if node.val >= max(path):
                cal+=1
            good(node.left)
            good(node.right)
            path.pop()
        good(root)
        return cal
            