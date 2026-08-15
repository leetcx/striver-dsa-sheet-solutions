class Solution:
    def findClosestElements(self, nums: List[int], k: int, x: int) -> List[int]:
        n=len(nums)
        ans=[]
       
        for i in range(n):
            ans.append((nums[i],abs(x-nums[i])))
        ans.sort(key=lambda x:x[1])
        subarr=ans[0:k]
        po=[]
        for i in range(len(subarr)):
            po.append(subarr[i][0])
        po.sort()
        return po

        


