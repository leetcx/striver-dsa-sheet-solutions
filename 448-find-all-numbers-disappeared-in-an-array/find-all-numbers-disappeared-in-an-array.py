class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        set1={}
        res=[0]* len(nums)
        
        for i in nums:
            if i in set1:
                set1[i]+=1
            else:
                set1[i]=1
        for i in range(len(nums)):
            res[i]=i+1
        z=[]
        for p in res:
            if p not in set1:
                z.append(p)
        return z
        
