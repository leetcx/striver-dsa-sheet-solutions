# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root==None:
            return []
        ans=[]
        q=deque()
        q.append(root)
        while q:
            lvl=len(q)
            temp=[]
            while lvl>0:
                p = q.popleft()
               
                temp.append(p.val)
                if p.left:
                    q.append(p.left)
                if p.right:
                    q.append(p.right)
                lvl-=1
            ans.append(temp)
        return ans
        