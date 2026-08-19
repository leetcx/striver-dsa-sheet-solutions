# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if root==None:
            return None
        ans=False
        q=deque()
        q.append(root)
        while q:
            p=len(q)
            while p:
                t=q.popleft()
                if t==None:
                    ans=True
                else:
                    if ans:
                        return False
                if t!=None:
                    q.append(t.left)
                

                    q.append(t.right)
                p-=1
        return ans
            

