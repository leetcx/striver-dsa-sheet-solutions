# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        def check(p,q):
            if p==None and q==None:
                return True
            if p==None or q==None:
                return False
            if p.val!=q.val:
                return False
            return check(p.left,q.left) and check(p.right,q.right)
        def find(curr):
            if curr==None :
                return False
            if curr.val==subRoot.val:
                if check(curr,subRoot):
                    return True
            left=find(curr.left)
            right=find(curr.right)
            return left or right
        return find(root)