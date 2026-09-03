class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atmost(k):
            low=0
            odd=0
            count=0
            for high in range(len(nums)):
                if nums[high] %2==1:
                    odd+=1
                while odd>k and low<=high:
                    if nums[low]%2==1:
                        odd-=1
                    low+=1
                count+=high-low+1
            return count
        return atmost(k)-atmost(k-1)
        
        
