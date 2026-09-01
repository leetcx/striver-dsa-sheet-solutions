class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        res= float('-inf')
        low=0
        high=0
        seto={}
        score=0
        for high in range(len(nums)):
            if nums[high] in seto:
                seto[nums[high]]+=1
            else:
                seto[nums[high]]=1
            score+=nums[high]
            lou=high-low+1
            while len(seto) < lou:
                seto[nums[low]]=seto.get(nums[low],0)-1
                if seto[nums[low]]==0:
                    del seto[nums[low]]
                score-=nums[low]
                low+=1
                lou=high-low+1
            if len(seto)==lou:
                res=max(res,score)
        if res==float('-inf'):
            return 0
        return res
