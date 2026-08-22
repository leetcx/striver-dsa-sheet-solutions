# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        ans = False

        def check(tree, kai):
           

            if tree == None and kai == None:
                return True

            if tree == None or kai == None:
                
                return False

            if tree.val != kai.val:
               
                return False

            return check(tree.left, kai.left) and check(tree.right, kai.right)

        def find(node):
            nonlocal ans

            if node == None:
                return

            if node.val == subRoot.val:
                if check(node, subRoot):
                    ans = True

            find(node.left)
            find(node.right)

        find(root)
        return ans