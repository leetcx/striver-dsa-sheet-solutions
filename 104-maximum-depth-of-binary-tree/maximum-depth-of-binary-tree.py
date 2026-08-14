
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def depth(node):
            if node==None:
                return 0
            p=depth(node.left)
            c=depth(node.right)

            return 1 + max(p,c)
        return depth(root)