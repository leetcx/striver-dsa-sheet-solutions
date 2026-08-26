# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root==None:
            return []
        q=deque()
        q.append(root)
        ans=[]
        while q:
            p=len(q)
            temp=[]
            while p:
                t=q.popleft()
                temp.append(t.val)
                if t.left !=None :
                    q.append(t.left)
                if t.right != None:
                    q.append(t.right)
                p-=1
            m=temp[-1]
            ans.append(m)
        return ans