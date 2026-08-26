class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        d=[[float(inf)] *2 for _ in range(n) ]
        def money(i,free,nums,n):
            nonlocal d
            if i==n:
                return 0
            if free==0:
                return money(i+1,1,nums,n)
            if d[i][free] != float('inf'):
                return d[i][free] 
            c1=nums[i]+ money(i+1,0,nums,n)
            c2=money(i+1,1,nums,n)
            p=max(c1,c2)
            d[i][free]=p
            return p
        return money(0,1,nums,len(nums))