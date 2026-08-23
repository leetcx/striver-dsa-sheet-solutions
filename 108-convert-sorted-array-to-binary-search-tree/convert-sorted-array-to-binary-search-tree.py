# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        p=len(nums)
        def const(low,high):
            if low> high:
                return 
            mid=(low+high)//2
            val=nums[mid]
            node=TreeNode(val)
            node.left=const(low,mid-1)
            node.right=const(mid+1,high)

            return node
        return const(0,len(nums)-1)
