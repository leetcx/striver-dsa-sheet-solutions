class Solution:
    def findSubsequences(self, nums: list[int]) -> list[list[int]]:
        temp=[]
        ans=[]
        set1={}
        def isvalid(arr):
            for p in range(len(arr)):
                if p>0 and arr[p]<arr[p-1]:
                    return False
            return True
        def put(i):
            nonlocal set1
            nonlocal temp
            nonlocal ans
            
            if i==len(nums):
                key=tuple(temp)
                if len(temp)>=2 and isvalid(temp):
                    key=tuple(temp)
                    if key not in set1:
                        set1[key]=1
                        ans.append(temp.copy())
                return
            

            temp.append(nums[i])
            
            put(i+1)
            temp.pop()
            put(i+1)
        put(0)
        return ans
