class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        set1={0:1}
        sum1=0
        count=0
        for i in range(len(nums)):
            sum1+=nums[i]
            prev=sum1-k
            if prev in set1:
                count+=set1[prev]
                
                
            
            
            if sum1 in set1:
                set1[sum1]+=1
            else:
                set1[sum1]=1
        return count
