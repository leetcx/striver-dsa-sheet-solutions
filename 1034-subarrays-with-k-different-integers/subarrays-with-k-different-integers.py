class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atmost(k):
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
                    
                
                
               
                count+=high-low+1
            return count
        return atmost(k)-atmost(k-1)
                