# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        q=deque()
        q.append(root)
        i=0
        ans=[]
        while q:
            s=len(q)
            temp=[]

            while s:
                p=q.popleft()
                temp.append(p.val)
                if p.right != None:
                    q.append(p.right)
                if p.left != None:
                    q.append(p.left)
                s-=1
            if i%2==0:
                temp.reverse()
            i+=1
            ans.append(temp)
        return ans


