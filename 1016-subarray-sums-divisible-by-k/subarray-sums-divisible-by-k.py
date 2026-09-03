class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        high=0
        sum1=0
        set1={0:1}
        ans=0
        for high in range(len(nums)):
            sum1+=nums[high]
            div=sum1%k
            if div in set1:
                ans+=set1[div]
                set1[div]+=1
                
                
            else:
                set1[div]=1
        return ans