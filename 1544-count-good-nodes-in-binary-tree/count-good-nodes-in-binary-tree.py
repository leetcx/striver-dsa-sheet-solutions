# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans=[]
       
        c=0
        def path(node):
            nonlocal ans
           
            nonlocal c
            if node==None:
                return
            ans.append(node.val)
            if node.val >=max(ans):
                c+=1
            path(node.left)
            
            
            path(node.right)
            ans.pop()
        path(root)
        return c

            