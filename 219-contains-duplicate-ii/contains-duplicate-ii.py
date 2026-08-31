class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        set1={}
        low=0
        for high in range(len(nums)):
            if nums[high] in  set1:
                if high - set1[nums[high]] <=k:
                    return True  
            
            set1[nums[high]]=high
        return False
        





