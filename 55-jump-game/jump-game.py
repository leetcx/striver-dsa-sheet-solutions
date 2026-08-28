class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach=0
        maxreach=0
        for i in range(len(nums)):
            if maxreach<i:
                return False
            reach=i+nums[i]
            maxreach=max(maxreach,reach)
            if maxreach >= len(nums)-1:
                return True
        return False
