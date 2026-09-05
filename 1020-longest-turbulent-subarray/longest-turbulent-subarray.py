class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        best=0
        count=1
        res=1
        c=0
        for i in range(1,len(arr)):
            if arr[i]>arr[i-1] and c !=1:
                count+=1
                c=1
            elif arr[i]<arr[i-1] and c!=-1 :
                count+=1
                c=-1
            else:
                res=max(res,count)

                if arr[i]==arr[i-1]:
                    count=1
                else:
                    count=2
        res=max(res,count)
        
        return res

