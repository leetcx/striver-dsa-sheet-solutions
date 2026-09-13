class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def find(mid):
            p=1
            sum1=0
            for i in nums:
                sum1+=i
                if sum1> mid:
                    p+=1
                    sum1=i
            return p
        low=max(nums)
        high=sum(nums)
        res=0
        while low<=high:
            mid=(low+high)//2
            z=find(mid)
            if z<=k:
                res=mid
                high=mid-1
            else:
                low=mid+1
        return res
        
            
