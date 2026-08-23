# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        sum1=0
        c=0
        def tar(node):
            nonlocal sum1
            nonlocal c
            if node== None:
                return 
            sum1+=node.val
            if sum1==targetSum:
                c+=1
            tar(node.left)
            tar(node.right)
            sum1-=node.val
        def find(node):
            if node==None:
                return 
            tar(node)

            find(node.left)
            find(node.right)
        find(root)
        return c
        
            