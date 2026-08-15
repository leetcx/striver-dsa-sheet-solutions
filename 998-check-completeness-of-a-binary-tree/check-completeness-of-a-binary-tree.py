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
            return True
        q=deque()
        q.append(root)
        bul=False
        while q:
            s=q.popleft()
            if s==None:
                bul=True
            else:
                if bul:
                    return False
                q.append(s.left)
                q.append(s.right)
        return True
       