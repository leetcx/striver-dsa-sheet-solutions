# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> list[TreeNode | None]:
        dp={}
        def do(n):
            if n%2==0 :
                return []
            if n==1:
                
                return [TreeNode(0)]
            state=(n)
            if state in dp:
                return dp[state]
            ans=[]
            for i in range(1,n,2):
                L=do(i)
                R=do(n-i-1)
                for nodel in L:
                    for zero in R:
                        root=TreeNode(0)
                        root.left=nodel
                        root.right=zero
                        ans.append(root)
            dp[state]= ans
            return dp[state]
        return do(n)
            


