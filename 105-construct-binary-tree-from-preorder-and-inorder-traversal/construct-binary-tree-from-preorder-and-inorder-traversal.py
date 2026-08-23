# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        set1={}  
        for i in range(len(inorder))  :
            set1[inorder[i]] =i
        preindex=0
        def const(low,high):
            nonlocal preindex
            nonlocal set1
            if low>high:
                return
            val=preorder[preindex]
            preindex+=1
            node=TreeNode(val)
            p=set1[val]
            node.left=const(low,p-1)
            node.right=const(p+1,high)
            return node
        return const(0,len(inorder)-1)
       

