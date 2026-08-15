# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        def searchroot(node1):
            if node1 == None:
                return None

            if node1.val == val:
                return node1

            left = searchroot(node1.left)
            if left != None:
                return left

            right = searchroot(node1.right)
            if right != None:
                return right

            return None

        return searchroot(root)