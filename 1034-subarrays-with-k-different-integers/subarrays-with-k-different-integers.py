class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        low=0
        high=0
        seto={}
        count=0
        c=0
        for high in range(len(nums)):
            if nums[high] in seto:
                seto[nums[high]]+=1
            else:
                seto[nums[high]]=1
            while len(seto) > k:
                seto[nums[low]]=seto.get(nums[low],0)-1
                if seto[nums[low]]==0:
                    del seto[nums[low]]
                low+=1
                c=0
            if len(seto)==k:
                
                while seto[nums[low]] >1:
                    seto[nums[low]]-=1
                    low+=1
                    c+=1
                count+=c+1
        return count
                