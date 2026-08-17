# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        set1={}
        for i in range(len(inorder)):
            set1[inorder[i]]=i
        preindex=len(postorder)-1
        def build(low,high):
            nonlocal preindex
            if low>high:
                return None
            val=postorder[preindex]
            preindex-=1

            root=TreeNode(val)
            p=set1[val]
            
            root.right=build(p+1,high)
            root.left=build(low,p-1)

            return root
        return build(0,len(inorder)-1)