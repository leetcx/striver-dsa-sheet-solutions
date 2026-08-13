# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root==None:
            return []
        ans=[]
        q=deque()
        q.append(root)
        i=0
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
            if i%2==1:
                temp.reverse()
            ans.append(temp)
               
            i+=1
            
        return ans
        