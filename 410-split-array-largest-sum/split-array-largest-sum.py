class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def count(mid):
            k=1
            sum1=nums[0]
            for i in range(1,len(nums)):
                if sum1+nums[i]>mid:
                    k+=1
                    sum1=nums[i]
                else:
                    sum1+=nums[i]
            return k
        low=max(nums)
        high=sum(nums)
        res=-1
        while low<=high:
            mid=(low+high)//2
            if count(mid)<=k:
                res=mid
                high=mid-1
            else:
                low=mid+1
        return res