# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans=[]
        sum1=0
        temp=[]
        def path(node):
            nonlocal ans
            nonlocal sum1
            nonlocal temp
            if node==None:
                return []
            sum1+=node.val
            temp.append(node.val)
            if node.left==None and node.right==None and sum1==targetSum:
                ans.append(temp.copy())
            path(node.left)
            path(node.right)
            sum1-=node.val
            temp.pop()
        path(root)
        return ans

