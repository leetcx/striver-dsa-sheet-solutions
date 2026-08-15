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
        q=deque()
        q.append(root)
        ans=[]
        while q:
            p=len(q)
            temp=[]
            while p:
                g=q.popleft()
                temp.append(g.val)
                if g.left !=None:
                    q.append(g.left)
                if g.right !=None:
                    q.append(g.right)
                p-=1
            ans.append(temp)
        return ans



        
