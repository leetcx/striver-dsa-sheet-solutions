class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        set1={0:1}
        sum1=0
        count=0
        for high in range(len(nums)):
            sum1+=nums[high]
            prev=(sum1 %k)%k
            if prev in set1:
                count+=set1[prev]
            if sum1 %k in set1:
                set1[sum1 % k] +=1
            else:
                set1[sum1 % k] =1
        return count