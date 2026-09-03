class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        balance=0
        set1={0:-1}
        res=float('-inf')
        for high in range(len(nums)):
            if nums[high]==0:
                balance-=1
            else:
                balance+=1
            if balance in set1:
                res=max(res,high-set1[balance])
            else:
                set1[balance]=high
        if res==float('-inf'):
            return 0
        return res
