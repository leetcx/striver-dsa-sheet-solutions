class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        low=0
        high=0
        sum1=0
        set1={0:1}
        ans=0
        for high in range(len(nums)):
            sum1+=nums[high]
            pref=sum1-k
            if pref in set1:
                ans+=set1[pref]
            set1[sum1] = set1.get(sum1, 0) + 1
        return ans
            