class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        low=0
        high=0
        res=float(-inf)
        n=len(nums)
        seto={}
        for high in range(0,n):
            if nums[high] in seto:
                seto[nums[high]]+=1
            else:
                seto[nums[high]]=1
            l=high-low+1
            p = seto.get(0, 0)
            while p>k:
                seto[nums[low]]-=1
                if seto[nums[low]]==0:
                    del seto[nums[low]]
                low+=1
                l=high-low+1
                p = seto.get(0, 0)
            l=high-low+1
            res=max(res,l)
        return res