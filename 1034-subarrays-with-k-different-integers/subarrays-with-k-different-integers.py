class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atmost(k):
            low=0
            high=0
            set1={}
            count=0
            for high in range(len(nums)):
                if nums[high] in set1:
                    set1[nums[high]]+=1
                else:
                    set1[nums[high]]=1
                while len(set1) > k:
                    set1[nums[low]]=set1.get(nums[low],0)-1
                    if set1[nums[low]]==0:
                        del set1[nums[low]]
                    low+=1
                count+=high-low+1
            return count
        return atmost(k)-atmost(k-1)
                
                